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

class ProjectAPI(object):
    """
    The project API endpoints used by the Rancher 2.x
    infra-structure.
    """
    def __init__(self, cli):
        self.type = "projects"
        self.cli = cli

    def list_projects(self, cluster):
        url = "clusters/%s/projects" % cluster
        contents = self.cli.get(url)
        return contents.data

    def get_project_by_name(self, cluster, name):
        url = "clusters/%s/projects?name=%s" % (cluster, name)
        contents = self.cli.get(url)
        return contents.data

    def get_project_by_id(self, cluster, id):
        url = "clusters/%s/projects?id=%s" % (cluster, id)
        contents = self.cli.get(url)
        return contents

    def delete_project(self, project_id):
        url = "projects/%s" % project_id
        contents = self.cli.delete(url)
        return contents

    def create_project(self, **kwargs):
        contents = self.cli.post(url=self.type, **kwargs)
        return contents

    def create_default_project(self, cluster_id, name):
        args = {
            "clusterId": cluster_id,
            "containerDefaultResourceLimit": None,
            "enableProjectMonitoring": False,
            "name": name,
            "namespaceDefaultResourceQuota": None,
            "namespaceId": "",
            "resourceQuota": None
        }

        contents = self.cli.post(self.type, args)
        return contents
    # def get_project_safe(self, cluster, id):
    #     contents = self.list_projects_name(cluster, id)
    #     if contents: return contents[0]
    #     return self.get_project(cluster, id)
