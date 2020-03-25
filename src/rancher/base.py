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

import requests
import collections
from requests.auth import HTTPBasicAuth

from . import cluster
from . import project
from . import client
from . import workload
from . import service
from . import namespace


class API(object):
    def __init__(self, *args, **kwargs):
        self.cli = client.RancherClient(*args, **kwargs)
        self.cluster_api = cluster.ClusterAPI(self.cli)
        self.project_api = project.ProjectAPI(self.cli)
        self.service_api = service.ServiceAPI(self.cli)
        self.workload_api = workload.WorkloadAPI(self.cli)
        self.namespace_api = namespace.NameSpaceAPI(self.cli)
