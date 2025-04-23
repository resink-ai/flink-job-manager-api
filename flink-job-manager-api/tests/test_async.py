import unittest

from flink_job_manager_api import Client
from flink_job_manager_api.api.default import get_cluster_overview, get_dashboard_configuration
from flink_job_manager_api.models import DashboardConfiguration

BASE_URL = "http://localhost:8081"


class TestAsyncCalls(unittest.IsolatedAsyncioTestCase):
    async def test_dashboard_configuration(self):
        async with Client(BASE_URL) as client:
            response: DashboardConfiguration = await get_dashboard_configuration.asyncio(client=client)
            print(f"Dashboard configuration: {response.to_dict()}")
            print(f"Flink version: {response.flink_version}")
            print(f"Flink revision: {response.flink_revision}")
            print(f"Features: {response.features}")
            print(f"Refresh interval: {response.refresh_interval}")
            print(f"Timezone name: {response.timezone_name}")
            print(f"Timezone offset: {response.timezone_offset}")
            

    async def test_cluster_overview(self):
        async with Client(BASE_URL) as client:
            response = await get_cluster_overview.asyncio(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"cluster overview response: {response.to_dict()}")
