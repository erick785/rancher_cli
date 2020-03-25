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

import json, time, re
import requests
from . import utils
from requests.auth import HTTPBasicAuth

BASE_URL = "https://39.102.45.64/v3/"
HEADERS = {'Accept': 'application/json'}


class RancherClient(object):
    def __init__(self, *args, **kwargs):
        self._base_url = kwargs.get("base_url", BASE_URL)
        self._access_key = kwargs.get("access_key", None)
        self._secret_key = kwargs.get("secret_key", None)
        self._headers = HEADERS.copy()
        self._auth = HTTPBasicAuth(self._access_key, self._secret_key)
        self._session = requests.sessions.session()
        self._session.verify = False

    def get(self, url, data=None):
        r = self._get_raw(self._base_url + url, data)
        return r.json(object_hook=utils.JSONObject)

    def post(self, url, data):
        r = self._post_raw(self._base_url + url, data)
        return r.json(object_hook=utils.JSONObject)

    def delete(self, url, data=None):
        r = self._delete_raw(self._base_url + url, data)
        return r.json(object_hook=utils.JSONObject)

    def _get_raw(self, url, data=None):
        return self._session.get(
            url,
            headers=self._headers,
            auth=self._auth,
        )

    def _post_raw(self, url, data):
        return self._session.post(
            url,
            json=data,
            auth=self._auth,
            headers=self._headers,
        )

    def _delete_raw(self, url, data=None):
        return self._session.delete(url,
                                    auth=self._auth,
                                    headers=self._headers)
