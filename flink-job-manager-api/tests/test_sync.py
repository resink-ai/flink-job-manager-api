import unittest

from flink_job_manager_api import Client
from flink_job_manager_api.api.default import get_cluster_overview, get_dashboard_configuration

BASE_URL = "http://localhost:8081"


class TestSyncCalls(unittest.TestCase):
    def test_cluster_overview(self):
        with Client(BASE_URL) as client:
            response = get_cluster_overview.sync(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"cluster overview response: {response.to_dict()}")

    def test_dashboard_configuration(self):
        with Client(BASE_URL) as client:
            response = get_dashboard_configuration.sync(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"dashboard configuration response: {response.to_dict()}")
