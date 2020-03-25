#!/usr/bin/python
# -*- coding: utf-8 -*-
# !/usr/bin/python
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

import json
from src import rancher

if __name__ == "__main__":
    api = rancher.API(secret_key="tcf5xjdllm5z82l2c6rqljpcqlfr9j9qd2hqq7rhgbcwkq9hnlmvql", access_key="token-r5n5h")
    # cluster
    clusters = api.cluster_api.list_clusters()
    # print("get_cluster_by_name", api.cluster_api.get_cluster_by_name("demo5"))
    # print("get_cluster_by_id", api.cluster_api.get_cluster_by_id("c-7x8mp"))
    # print("add_nodes", api.cluster_api.add_nodes("c-7x8mp"))
    # print("create_default_cluster", api.cluster_api.create_default_cluster("t1-cluster"))
    # print("delete_cluster", api.cluster_api.delete_cluster("c-cslx9"))
    #
    # # project
    # print("list_projects", api.project_api.list_projects("c-7x8mp"))
    # print("get_project_by_name", api.project_api.get_project_by_name("c-7x8mp", "Default"))
    # print("get_project_by_id", api.project_api.get_project_by_id("c-7x8mp", "c-7x8mp:p-j5l28"))
    # print("create_default_project", api.project_api.create_default_project("c-7x8mp", "t1-project"))
    # print("delete_project", api.project_api.delete_project("c-7x8mp:p-6ljss"))

    #
    # # namespace
    #
    # # workload
    # print("list_workloads", api.workload_api.list_workloads("c-7x8mp:p-j5l28"))
    # print("get_workloads_by_name", api.workload_api.get_workload_by_name("c-7x8mp:p-j5l28", "nginx"))
    # print("get_workload_by_id", api.workload_api.get_workload_by_id("c-7x8mp:p-j5l28", "deployment:default:nginx"))
    # print("create_default_workload", api.workload_api.create_default_workload("ntk", "c-7x8mp:p-j5l28", 10, "172.17.127.96 172.17.127.97"))
    print("create_default_workload", api.workload_api.create_default_workload("ntk", "c-7x8mp:p-j5l28", 10, "39.102.45.64 39.102.43.24"))
    # print("delete_workload", api.workload_api.delete_workload("c-7x8mp:p-j5l28", "daemonset:default:nginx2"))

    # print("create_workload", api.workload_api.create_workload("c-7x8mp:p-j5l28", {
    #     "hostIPC": False,
    #     "hostNetwork": False,
    #     "hostPID": False,
    #     "paused": False,
    #     "type": "workload",
    #     "namespaceId": "default",
    #     "scale": 1,
    #     "dnsPolicy": "ClusterFirst",
    #     "restartPolicy": "Always",
    #     "labels": {},
    #     "containers": [{
    #         "initContainer": False,
    #         "restartCount": 0,
    #         "stdin": True,
    #         "stdinOnce": False,
    #         "tty": True,
    #         "type": "container",
    #         "privileged": False,
    #         "allowPrivilegeEscalation": False,
    #         "readOnly": False,
    #         "runAsNonRoot": False,
    #         "namespaceId": "default",
    #         "imagePullPolicy": "Always",
    #         "environmentFrom": [],
    #         "resources": {
    #             "requests": {},
    #             "limits": {}
    #         },
    #         "capAdd": [],
    #         "capDrop": [],
    #         "image": "39.102.43.24:30003/test/nginx",
    #         "ports": [{
    #             "containerPort": 80,
    #             "hostPort": 0,
    #             "type": "containerPort",
    #             "kind": "NodePort",
    #             "protocol": "TCP",
    #             "name": "pp"
    #         }],
    #         "livenessProbe": None,
    #         "name": "nginx4",
    #         "volumeMounts": []
    #     }],
    #     "scheduling": {
    #         "node": {}
    #     },
    #     "deploymentConfig": {
    #         "minReadySeconds": 0,
    #         "type": "deploymentConfig",
    #         "revisionHistoryLimit": 10,
    #         "strategy": "RollingUpdate",
    #         "maxSurge": 1,
    #         "maxUnavailable": 0
    #     },
    #     "name": "nginx4",
    #     "annotations": {
    #         "cattle.io/timestamp": "2020-03-05T06:16:14Z"
    #     },
    #     "volumes": []
    # }))
