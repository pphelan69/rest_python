import logging
import pytest
import json
import datacloud.macromanager
from miscutils import file_utils
from tests.base_test import BaseTest


@pytest.mark.run(order=8)
@pytest.mark.usefixtures("setup")
class TestUpdateMacros(BaseTest):

    @staticmethod
    def macrosets_postdata():
        mypath = file_utils.get_auto_loc_root() + "dc_integ_auto/config/payloads/macrosets_create_1.json"
        with open(mypath) as payload:
            reqpayload = json.load(payload)
            return reqpayload

    @pytest.fixture(scope="class")
    def macrosets_update(self, request):
        postdata = self.macrosets_postdata()
        postdata["value"] = "c:\logs\data"
        return datacloud.macromanager.UpdateMacroSetAPI(request.cls.dc_host, request.cls.dc_usersid_1, postdata["name"],
                                                        request.cls.dc_token, request.cls.dc_account1_id,
                                                        payload=postdata)

    # Has a dependency on there being at least 1 macro in existance.
    def test_macrosets_post_test1(self, macrosets_update):
        logging.info("Test to see we can create a global macro")
        expect_value = "Macro1"
        actual_value = macrosets_update.get_name()
        err_msg = "Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)
