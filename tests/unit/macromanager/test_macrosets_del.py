import logging
import pytest
import json
import datacloud.macromanager
from miscutils import file_utils
from tests.base_test import BaseTest


@pytest.mark.run(order=-3)
@pytest.mark.usefixtures("setup")
class TestDeleteMacros(BaseTest):

    @staticmethod
    def macrosets_postdata():
        mypath = file_utils.get_auto_loc_root() + "dc_integ_auto/config/payloads/macrosets_create_1.json"
        with open(mypath) as payload:
            reqpayload = json.load(payload)
            return reqpayload

    @pytest.fixture(scope="class")
    def macrosets_delete(self, request):
        postdata = self.macrosets_postdata()
        print(postdata["name"])
        return datacloud.macromanager.DeleteMacroSetAPI(request.cls.dc_host, request.cls.dc_usersid_1, postdata["name"],
                                                        request.cls.dc_token, request.cls.dc_account1_id)

    # Has a dependency on there being at least 1 macro in existance.
    def test_macrosets_delete_test1(self, macrosets_delete):
        logging.info("Test to see we can delete a global macro")
        expect_value = "Macro Deleted"
        actual_value = macrosets_delete.delete_status()
        err_msg = "Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)
