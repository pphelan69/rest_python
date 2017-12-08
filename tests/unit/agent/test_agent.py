import logging
import datacloud.agent
import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestAgent(BaseTest):

    @pytest.fixture(scope="class")
    def show_all_agents(self, request):
        agent = datacloud.agent.GetAgentAPI(request.cls.dc_host, request.cls.dc_token)
        return agent

    def test_agents_1(self, show_all_agents):
        logging.info("Unit Testing: /v2/agents get api response")

        expect_value = True
        actual_value = self.dc_agent1 in show_all_agents.get_agent_list()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
