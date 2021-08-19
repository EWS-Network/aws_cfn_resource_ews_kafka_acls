#  -*- coding: utf-8 -*-
# SPDX-License-Identifier: MPL-2.0
# Copyright 2021 John Mille<john@ews-network.net>

import logging
from typing import Any, MutableMapping, Optional

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
    identifier_utils,
)

from .acls_management import create_new_acls, delete_acls
from .common import differentiate_old_new_acls
from .models import ResourceHandlerRequest, ResourceModel

LOG = logging.getLogger(__name__)
TYPE_NAME = "EWS::Kafka::Topic"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


def get_cluster_config(model):
    """

    :param model:
    :return:
    """
    cluster_config = {
        "bootstrap_servers": model.BootstrapServers,
        "security_protocol": model.SecurityProtocol,
        "sasl_mechanism": model.SASLMechanism,
        "sasl_plain_username": model.SASLUsername,
        "sasl_plain_password": model.SASLPassword,
    }
    return cluster_config


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    cluster_config = get_cluster_config(model)
    try:
        primary_identifier = None
        if primary_identifier is None:
            primary_identifier = identifier_utils.generate_resource_identifier(
                stack_id_or_name=request.stackId,
                logical_resource_id=request.logicalResourceIdentifier,
                client_request_token=request.clientRequestToken,
                max_length=255,
            )
        create_new_acls(list(model.Policies), cluster_config)
        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"was not expecting type {str(e)}"
        )
    return read_handler(session, request, callback_context)


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    old_model = request.previousResourceState
    cluster_config = get_cluster_config(model)
    acls = differentiate_old_new_acls(list(model.Policies), list(old_model.Policies))
    try:
        delete_acls(acls[1], cluster_config)
        create_new_acls(acls[0], cluster_config)
    except Exception as error:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"Failed to update ACLs {str(error)}"
        )
    return read_handler(session, request, callback_context)


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    cluster_config = get_cluster_config(model)
    try:
        delete_acls(model.Policies, cluster_config)
        return progress
    except Exception as error:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"was not expecting type {str(error)}"
        )


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
