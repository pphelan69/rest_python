import logging
import json
import datacloud.jobconfiguration
from miscutils import file_utils
import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=-3)
class TestDeleteConfigAPI(BaseTest):

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
    def delete_jobconfig(self, request):
        jobconfigid = self.read_jobconfigdata()
        return datacloud.jobconfiguration.DeleteConfigAPI(request.cls.dc_host, request.cls.dc_token,
                                                          config_id=jobconfigid)

    def test_create_config1(self, delete_jobconfig):
        logging.info("Deleted Job Config of a Template")
        logging.info(delete_jobconfig.del_config_status())

