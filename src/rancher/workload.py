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

import os
import json
import datetime
from .utils import JSONObject


class WorkloadAPI(object):
    """
    The workload API endpoints used by the Rancher 2.x
    infra-structure.
    """

    def __init__(self, cli):
        self.type = "workloads"
        self.cli = cli

    def list_workloads(self, project, *args, **kwargs):
        url = "projects/%s/workloads" % project
        contents = self.cli.get(url, **kwargs)
        return contents.data

    def get_workload_by_name(self, project, name):
        url = "projects/%s/workloads?name=%s" % (project, name)
        contents = self.cli.get(url)
        return contents

    def get_workload_by_id(self, project, id):
        url = "projects/%s/workloads/%s" % (project, id)
        contents = self.cli.get(url)
        return contents

    def update_workload(self, project, id, payload={}):
        url = self.base_url + "projects/%s/workloads/%s" % (project, id)
        contents = self.cli.post(url, data_j=payload)
        return contents

    def upgrade_workload(self, project, id):
        workload = self.get_workload(project, id)
        current_date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
        workload["annotations"]["cattle.io/timestamp"] = current_date
        self.update_workload(project, id, payload=workload)
        return workload

    def delete_workload(self, project_id, work_load_name):
        url = "project/%s/workloads/%s" % (project_id, work_load_name)
        contents = self.cli.delete(url)
        return contents

    def create_workload(self, project_id, payload={}):
        url = "projects/%s/workload" % project_id
        contents = self.cli.post(url, payload)
        return contents

    def create_default_workload(self, name, project_id, block_interval, ips):
        tpl_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "model\default.json")
        with open(tpl_path, mode='r', encoding='utf-8') as fp:
            setttings = fp.read()

        setttings = json.loads(setttings)
        setttings["name"] = name
        setttings["projectId"] = project_id
        setttings["containers"][0]["name"] = name
        setttings["containers"][0]["environment"]["BLOCK_INTERVAL"] = block_interval
        setttings["containers"][0]["environment"]["IP"] = ips

        url = "projects/%s/workload" % project_id
        contents = self.cli.post(url, setttings)
        return contents
