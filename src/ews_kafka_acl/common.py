#  -*- coding: utf-8 -*-
# SPDX-License-Identifier: MPL-2.0
# Copyright 2021 John Mille<john@ews-network.net>

"""Common functions """

import logging


LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


def keyisset(x, y):
    """
    Macro to figure if the the dictionary contains a key and that the key is not empty

    :param x: The key to check presence in the dictionary
    :type x: str
    :param y: The dictionary to check for
    :type y: dict

    :returns: True/False
    :rtype: bool
    """
    if isinstance(y, dict) and x in y.keys() and y[x]:
        return True
    return False


def keypresent(x, y):
    """
    Macro to figure if the the dictionary contains a key and that the key is not empty

    :param x: The key to check presence in the dictionary
    :type x: str
    :param y: The dictionary to check for
    :type y: dict

    :returns: True/False
    :rtype: bool
    """
    if isinstance(y, dict) and x in y.keys():
        return True
    return False


def differentiate_old_new_acls(new_policies, old_policies):
    """
    Function to differentiate with ACLs are common and shall be kept, which ones are to be added and then removed.

    :param list new_policies:
    :param list old_policies:
    :return: the new acls and old acls
    :rtype: tuple
    """

    common_policies = [d for d in new_policies if d in old_policies]
    LOG.info("Common policies")
    LOG.info(common_policies)
    common_policies_set = set()
    for policy in common_policies:
        common_policies_set.add(tuple(policy.items()))
    new_policies_set = set()
    old_policies_set = set()
    for policy in new_policies:
        t_policy = tuple(policy.items())
        if t_policy not in new_policies_set or t_policy in common_policies:
            new_policies_set.add(t_policy)
    for policy in old_policies:
        t_policy = tuple(policy.items())
        if (
            t_policy not in old_policies_set
            and t_policy not in common_policies
            and t_policy not in new_policies_set
        ):
            old_policies_set.add(t_policy)
    final_delete_acls = [dict(k) for k in old_policies_set]
    final_new_acls = [dict(k) for k in new_policies_set]
    return final_new_acls, final_delete_acls
