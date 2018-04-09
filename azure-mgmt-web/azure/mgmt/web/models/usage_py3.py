# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_only_resource import ProxyOnlyResource


class Usage(ProxyOnlyResource):
    """Usage of the quota resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar display_name: Friendly name shown in the UI.
    :vartype display_name: str
    :ivar usage_name: Name of the quota.
    :vartype usage_name: str
    :ivar resource_name: Name of the quota resource.
    :vartype resource_name: str
    :ivar unit: Units of measurement for the quota resource.
    :vartype unit: str
    :ivar current_value: The current value of the resource counter.
    :vartype current_value: long
    :ivar limit: The resource limit.
    :vartype limit: long
    :ivar next_reset_time: Next reset time for the resource counter.
    :vartype next_reset_time: datetime
    :ivar compute_mode: Compute mode used for this usage. Possible values
     include: 'Shared', 'Dedicated', 'Dynamic'
    :vartype compute_mode: str or ~azure.mgmt.web.models.ComputeModeOptions
    :ivar site_mode: Site mode used for this usage.
    :vartype site_mode: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'display_name': {'readonly': True},
        'usage_name': {'readonly': True},
        'resource_name': {'readonly': True},
        'unit': {'readonly': True},
        'current_value': {'readonly': True},
        'limit': {'readonly': True},
        'next_reset_time': {'readonly': True},
        'compute_mode': {'readonly': True},
        'site_mode': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'usage_name': {'key': 'properties.name', 'type': 'str'},
        'resource_name': {'key': 'properties.resourceName', 'type': 'str'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'current_value': {'key': 'properties.currentValue', 'type': 'long'},
        'limit': {'key': 'properties.limit', 'type': 'long'},
        'next_reset_time': {'key': 'properties.nextResetTime', 'type': 'iso-8601'},
        'compute_mode': {'key': 'properties.computeMode', 'type': 'ComputeModeOptions'},
        'site_mode': {'key': 'properties.siteMode', 'type': 'str'},
    }

    def __init__(self, *, kind: str=None, **kwargs) -> None:
        super(Usage, self).__init__(kind=kind, **kwargs)
        self.display_name = None
        self.usage_name = None
        self.resource_name = None
        self.unit = None
        self.current_value = None
        self.limit = None
        self.next_reset_time = None
        self.compute_mode = None
        self.site_mode = None
