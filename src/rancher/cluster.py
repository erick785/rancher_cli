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


class ClusterAPI(object):
    """
    The cluster API endpoints used by the Rancher 2.x infra-structure.
    """

    def __init__(self, cli):
        self.type = "clusters"
        self.cli = cli

    def list_clusters(self, *args, **kwargs):
        url = self.type
        contents = self.cli.get(url, **kwargs)
        return contents.data

    def get_cluster_by_name(self, name):
        url = "%s?name=%s" % (self.type, name)
        contents = self.cli.get(url)
        if len(contents.data) > 0:
            return contents.data[0]
        return None

    def get_cluster_by_id(self, id):
        contents = None
        try:
            url = "%s/%s" % (self.type, id)
            contents = self.cli.get(url)
        except utils.ApiError as e:
            print(e)
        return contents

    def create_cluster(self, name, **kwargs):
        contents = self.cli.post(self.type, **kwargs)
        return contents

    def create_default_cluster(self, name):
        default_args = {
            "amazonElasticContainerServiceConfig": None,
            "answers": None,
            "azureKubernetesServiceConfig": None,
            "dockerRootDir": "/var/lib/docker",
            "enableClusterAlerting": False,
            "enableClusterMonitoring": False,
            "googleKubernetesEngineConfig": None,
            "localClusterAuthEndpoint": None,
            "name": name,
            "rancherKubernetesEngineConfig": {},
            "windowsPreferedCluster": False,
        }

        contents = self.cli.post(self.type, default_args)
        return contents

    def delete_cluster(self, cluster_id):
        url = "%s/%s" % (self.type, cluster_id)
        contents = self.cli.delete(url)
        return contents

    def add_nodes(self, cluster_id, node_name="", name_space_id=""):
        url = "clusterregistrationtokens"
        args = {
            "clusterId": cluster_id,
            "name": node_name,
            "namespaceId": name_space_id
        }

        contents = self.cli.post(url, args)
        return contents
