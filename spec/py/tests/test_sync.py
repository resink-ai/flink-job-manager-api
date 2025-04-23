import unittest

from flink_job_manager_api import Client
from flink_job_manager_api.api.default import get_cluster_overview, get_dashboard_configuration
from flink_job_manager_api.models import ClusterOverviewWithVersion

BASE_URL = "http://localhost:8081"


class TestSyncCalls(unittest.TestCase):
    def test_cluster_overview(self):
        with Client(BASE_URL) as client:
            response: ClusterOverviewWithVersion = get_cluster_overview.sync(client=client)
            print(f"Cluster overview: {response.to_dict()}")
            print(f"Flink version: {response.flink_version}")
            print(f"Flink commit: {response.flink_commit}")
            print(f"Jobs cancelled: {response.jobs_cancelled}")
            print(f"Jobs failed: {response.jobs_failed}")
            print(f"Jobs finished: {response.jobs_finished}")
            print(f"Jobs running: {response.jobs_running}")
            print(f"Slots available: {response.slots_available}")
            print(f"Slots free and blocked: {response.slots_free_and_blocked}")
            print(f"Slots total: {response.slots_total}")
            print(f"Taskmanagers: {response.taskmanagers}")
            print(f"Taskmanagers blocked: {response.taskmanagers_blocked}")

    def test_dashboard_configuration(self):
        with Client(BASE_URL) as client:
            response = get_dashboard_configuration.sync(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"dashboard configuration response: {response.to_dict()}")
