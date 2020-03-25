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

import time

class ServiceAPI(object):
    """
    The service API endpoints used by the Rancher 1.x
    infra-structure.
    """
    def __init__(self, cli):
        self.type = "clusters"
        self.srv_api = cli

    def list_services(self, *args, **kwargs):
        url = self.base_url + "services"
        contents = self.get(url, **kwargs)
        data = contents["data"]
        return data

    def list_services_name(self, name, stack = None):
        url = self.base_url + "services?name=%s" % name
        if stack: url += "&stackId=%s" % stack
        contents = self.get(url)
        data = contents["data"]
        return data

    def get_service(self, id):
        url = self.base_url + "services/%s" % id
        contents = self.get(url)
        return contents

    def get_service_safe(self, id, stack = None):
        contents = self.list_services_name(id, stack = stack)
        if contents: return contents[0]
        return self.get_service(id)

    def update_service(self, id, payload = {}):
        url = self.base_url + "services/%s" % id
        contents = self.put(url, data_j = payload)
        data = contents["data"]
        return data

    def upgrade_service(
        self,
        id,
        batch_size = 1,
        interval = 2000,
        full_upgrade = True,
        try_finish = True,
        safe = True,
        launch_config = None
    ):
        url = self.base_url + "services/%s?action=upgrade" % id
        if try_finish: self._service_try_finish(id)
        if launch_config == None: launch_config = self._service_launch_config(id)
        if safe and not self._service_active(id):
            raise appier.OperationalError(
                message = "Service is currently not ready for upgrade"
            )
        contents = self.post(
            url,
            data_j = dict(
                inServiceStrategy = dict(
                    batchSize = batch_size,
                    intervalMillis = interval,
                    fullUpgrade = full_upgrade,
                    launchConfig = launch_config,
                    secondaryLaunchConfigs = []
                )
            )
        )
        data = contents["data"]
        return data

    def finish_upgrade_service(self, id):
        url = self.base_url + "services/%s?action=finishupgrade" % id
        contents = self.post(url)
        data = contents["data"]
        return data

    def rollback_service(self, id):
        url = self.base_url + "services/%s?action=rollback" % id
        contents = self.post(url)
        data = contents["data"]
        return data

    def restart_service(self, id, batch_size = 1, interval = 2000):
        url = self.base_url + "services/%s?action=restart" % id
        contents = self.post(
            url,
            data_j = dict(
                rollingRestartStrategy = dict(
                    batchSize = batch_size,
                    intervalMillis = interval
                )
            )
        )
        data = contents["data"]
        return data

    def _service_active(self, id):
        service = self.get_service(id)
        return service["state"] == "active"

    def _service_upgraded(self, id):
        service = self.get_service(id)
        return service["state"] == "upgraded"

    def _service_try_finish(self, id, timeout = 10.0, force = False):
        if not self._service_upgraded(id) and not force: return
        try: self.finish_upgrade_service(id)
        except Exception: pass
        else: time.sleep(timeout)

    def _service_launch_config(self, id):
        service = self.get_service(id)
        data = service.get("data", {})
        fields = data.get("fields", {})
        launch_config = fields.get("launchConfig", {})
        return launch_config

    def _service_image_uuid(self, id):
        launch_config = self._service_launch_config(id)
        image_uuid = launch_config.get("imageUuid", None)
        return image_uuid
