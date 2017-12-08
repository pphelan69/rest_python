import logging
import json
import datacloud.accountmanager
import pytest
from miscutils import file_utils
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestUpdateUserID(BaseTest):

    @staticmethod
    def userid_postdata():
        # Read the Request Payload for the Create Job Template API
        mypath = file_utils.get_auto_loc_root() + "dc_integ_auto/config/payloads/usersid_update_1.json"
        logging.info("Request Payload for Update user id")
        logging.info(mypath)
        with open(mypath) as payload:
            reqpayload = json.load(payload)
            return reqpayload

    @pytest.fixture(scope="class")
    def userid_fixture1(self, request):
        postdata = self.userid_postdata()
        userid = datacloud.accountmanager.UpdateUserIDAPI(request.cls.dc_host, request.cls.dc_token,
                                                          request.cls.dc_usersid_2, payload=postdata)
        return userid

    def test_usersid_update1(self, userid_fixture1):
        logging.info("Unit Testing: /v2/users/{user_id} put api response - username")

        expect_value = "Internal server error"
        actual_value = userid_fixture1.get_msg()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
