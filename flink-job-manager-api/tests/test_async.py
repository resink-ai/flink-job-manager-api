import unittest

from flink_job_manager_api import Client
from flink_job_manager_api.api.default import get_cluster_overview, get_dashboard_configuration

BASE_URL = "http://localhost:8081"


class TestAsyncCalls(unittest.IsolatedAsyncioTestCase):
    async def test_dashboard_configuration(self):
        async with Client(BASE_URL) as client:
            response = await get_dashboard_configuration.asyncio(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"dashboard configuration response: {response.to_dict()}")

    async def test_cluster_overview(self):
        async with Client(BASE_URL) as client:
            response = await get_cluster_overview.asyncio(client=client)
            self.assertIsNotNone(response.to_dict())
            print(f"cluster overview response: {response.to_dict()}")
