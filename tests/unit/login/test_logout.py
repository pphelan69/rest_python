import logging
import datacloud.login
import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestLogout(BaseTest):

    # "Logout" Fixtures
    @pytest.fixture(scope="class")
    def good_logout(self, request):
        return datacloud.login.CreateLogoutAPI(request.cls.dc_host, request.cls.dc_token)

    @pytest.fixture(scope="class")
    def bad_logout1(self, request):
        return datacloud.login.CreateLogoutAPI(request.cls.dc_host,
                                               "Bearer: NzYwNTAzOGUtMWFhMy00MjEzLWE3YmItMjBkNmE1OWIxZTg4")

    @pytest.fixture(scope="class")
    def bad_logout2(self, request):
        return datacloud.login.CreateLogoutAPI(request.cls.dc_host, "")

    def test_logout1(self, good_logout):
        logging.info("Testing that the Logout was Successful")
        expect_value = True
        actual_value = good_logout.get_logout_msg()
        err_msg = "Did not logout successfully: - Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_logout2(self, bad_logout1):
        logging.info("Testing that the correct Logout Error is Received in case of an Expired Token")
        expect_value = "DX_EXCEPTION: BAD_REQ: Logout failed."
        actual_value = bad_logout1.get_logout_errmsg()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_logout3(self, bad_logout2):
        logging.info("Testing that the correct Logout Error is Received when authorization header is not passed")
        expect_value = "DX_EXCEPTION: BAD_REQ: Missing required Header parameters: [Authorization]"
        actual_value = bad_logout2.get_logout_errmsg()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
