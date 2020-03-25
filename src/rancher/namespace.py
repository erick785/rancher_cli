#!/usr/bin/python
# -*- coding: utf-8 -*-

# Rocky Rancher API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Rocky Rancher API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Rocky Rancher API. If not, see <http://www.apache.org/licenses/>.

from . import utils


class NameSpaceAPI(object):
    """
    The cluster API endpoints used by the Rancher 2.x infra-structure.
    """

    def __init__(self, cli):
        self.type = "namespaces"
        self.cli = cli

    def list_namespace(self, cluster_id):
        url = "cluster/%s/namespaces" % (cluster_id)
        content = self.cli.get(url)
        return content

    def get_namespace_by_name(self, cluster_id, name):
        url = "cluster/%s/namespaces?name=%s" % (cluster_id, name)
        content = self.cli.get(url)
        return content

    def create_namespace(self, name, cluster_id, **kwargs):
        kwargs["name"] = name
        url = "cluster/%s/namespaces" % cluster_id
        content = self.cli.post(url, **kwargs)
        return content

    def create_default_namespace(self, name, cluster_id, project_id):
        kwargs = {
            "containerDefaultResourceLimit": None,
            "name": name,
            "projectId": project_id,
            "resourceQuota": None
        }

        url = "cluster/%s/namespaces" % cluster_id
        content = self.cli.post(url, **kwargs)

        return content
