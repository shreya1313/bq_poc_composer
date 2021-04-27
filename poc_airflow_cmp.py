#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example Airflow DAG for Google Kubernetes Engine.
"""

import os

from airflow import models
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.kubernetes_engine import (
    GKECreateClusterOperator,
    GKEDeleteClusterOperator,
    GKEStartPodOperator,
)
from airflow.utils.dates import days_ago

GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID", "graphical-elf-309911")
GCP_LOCATION = os.environ.get("GCP_GKE_LOCATION", "us-central1-a")
CLUSTER_NAME = os.environ.get("GCP_GKE_CLUSTER_NAME", "my-cluster")

# [START howto_operator_gcp_gke_create_cluster_definition]
# CLUSTER = {"name": CLUSTER_NAME, "initial_node_count": 1}
# [END howto_operator_gcp_gke_create_cluster_definition]

with models.DAG(
    "example_gcp_gke",
    schedule_interval=None,  # Override to match your needs
    start_date=days_ago(1),
    tags=['example'],
) as dag:
    # [START gke_start_pod_operator]
    pod_task_dev = GKEStartPodOperator(
        task_id="create_pod_task_dev",
        project_id=GCP_PROJECT_ID,
        location=GCP_LOCATION,
        cluster_name=CLUSTER_NAME,
        namespace="dev",
        image="gcr.io/graphical-elf-309911/demoapp1",
        image_pull_policy='Always',
        name="airflow-test-pod-dev",
    )
    # [END gke_start_pod_operator]
    
    pod_task_test = GKEStartPodOperator(
        task_id="create_pod_task_test",
        project_id=GCP_PROJECT_ID,
        location=GCP_LOCATION,
        cluster_name=CLUSTER_NAME,
        namespace="test",
        image="gcr.io/graphical-elf-309911/bqapp",
        image_pull_policy='Always'
        name="airflow-test-pod-test",
    )

    pod_task_dev >> pod_task_test

