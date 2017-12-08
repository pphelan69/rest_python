import logging
import pytest
import datacloud.macromanager
from tests.base_test import BaseTest


@pytest.mark.run(order=9)
@pytest.mark.usefixtures("setup")
class TestGetMacros(BaseTest):

    @pytest.fixture(scope="class")
    def macrosets_get(self, request):
        return datacloud.macromanager.GetMacroSetAPI(request.cls.dc_host, request.cls.dc_token,
                                                     request.cls.dc_account1_id)

    # Has a dependency on there being at least 1 macro in existance.
    def test_macrosets_get_test1(self, macrosets_get):
        logging.info("Test to get all available macros and ensure you have at least one.")
        self.log_assert(macrosets_get.get_all_macro_names() > 0, "No macros exist.")

    # Has a dependency on there being a macro called "Macro1"
    def test_macrosets_get_test2(self, macrosets_get):
        logging.info("Test to ensure the value of the macro called Macro1 is correct.")
        expect_value = "c:\logs\data"
        actual_value = macrosets_get.get_macro_value("Macro1")
        err_msg = "Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

    # Has a dependency on there being a macro called "Macro1"
    def test_macrosets_get_test3(self, macrosets_get):
        logging.info("Test to ensure the macro called Macro1 is not secure.")
        expect_value = False
        actual_value = macrosets_get.is_macro_secure("Macro1")
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    # Has a dependency on there being a macro called "Macro1"
    def test_macrosets_get_test4(self, macrosets_get):
        logging.info("Test to ensure the macro called Macro1 has correct macroset id.")
        expect_value = "21610"
        actual_value = macrosets_get.get_macro_macroset("Macro1")
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
