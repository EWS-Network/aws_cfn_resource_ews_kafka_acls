#  -*- coding: utf-8 -*-
# SPDX-License-Identifier: MPL-2.0
# Copyright 2021 John Mille<john@ews-network.net>

"""
Module to handle Kafka topics management.
"""

from kafka.admin import (
    ACL,
    ACLFilter,
    ACLOperation,
    ACLPermissionType,
    ACLResourcePatternType,
    KafkaAdminClient,
    ResourcePattern,
    ResourcePatternFilter,
    ResourceType,
)


def create_new_acls(acls, cluster_info):
    """
    Function to iterate over the given ACL policies and apply them

    :param list acls:
    :param cluster_info:
    :return:
    """
    admin_client = KafkaAdminClient(**cluster_info)
    kafka_acls = []
    for policy in acls:
        if isinstance(policy, dict):
            new_acl = ACL(
                principal=policy["Principal"],
                host=policy["Host"],
                operation=ACLOperation[policy["Action"]],
                permission_type=ACLPermissionType[policy["Effect"]],
                resource_pattern=ResourcePattern(
                    resource_type=ResourceType[policy["ResourceType"]],
                    resource_name=policy["Resource"],
                    pattern_type=ACLResourcePatternType[policy["PatternType"]],
                ),
            )
            kafka_acls.append(new_acl)
    admin_client.create_acls(kafka_acls)


def delete_acls(acls, cluster_info):
    """
    Function to delete the ACLs.
    :param acls:
    :param cluster_info:
    :return:
    """
    admin_client = KafkaAdminClient(**cluster_info)
    policies = []
    for policy in acls:
        new_filter = ACLFilter(
            principal=policy["Principal"],
            host=policy["Host"] if "Host" in policy else "*",
            operation=ACLOperation[policy["Action"]],
            permission_type=ACLPermissionType[policy["Effect"]],
            resource_pattern=ResourcePatternFilter(
                resource_type=ResourceType[policy["ResourceType"]],
                resource_name=policy["Resource"],
                pattern_type=ACLResourcePatternType[policy["PatternType"]],
            ),
        )
        policies.append(new_filter)
    admin_client.delete_acls(policies)
