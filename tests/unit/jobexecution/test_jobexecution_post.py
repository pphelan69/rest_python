import logging
import pytest
import json
from miscutils import file_utils
import datacloud.jobexecution
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=5)
class TestPostJobExecutionAPI(BaseTest):

    @staticmethod
    def read_jobconfigdata():
        # Read the Response of the Create Job Config API
        mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobconfig.json"
        logging.info("Info Related to a Newly Created JobConfig")
        logging.info(mypath)
        with open(mypath) as payload:
            configdata = json.load(payload)
            logging.info(configdata["id"])
            return configdata["id"]

    @pytest.fixture(scope="class")
    def execute_jobconfig(self, request):
        jobconfigid = self.read_jobconfigdata()
        return datacloud.jobexecution.PostJobExecutionAPI(request.cls.dc_host, request.cls.dc_token,
                                                          config_id=jobconfigid)

    def test_execute_config1(self, execute_jobconfig):
        logging.info("Executing a Job Config for a Template")
        logging.info(execute_jobconfig.get_jobexecution_msg())
