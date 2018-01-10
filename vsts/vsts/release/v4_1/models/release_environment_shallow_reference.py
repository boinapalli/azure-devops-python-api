# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ReleaseEnvironmentShallowReference(Model):
    """ReleaseEnvironmentShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release environment.
    :type _links: :class:`ReferenceLinks <release.v4_1.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release environment.
    :type id: int
    :param name: Gets or sets the name of the release environment.
    :type name: str
    :param url: Gets the REST API url to access the release environment.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseEnvironmentShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url
