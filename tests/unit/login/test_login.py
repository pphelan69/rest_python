import logging
import datacloud.login
import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    # "Login" Fixtures
    @pytest.fixture(scope="class")
    def good_login(self, request):
        return datacloud.login.CreateLoginAPI(request.cls.dc_host, request.cls.dc_user, request.cls.dc_pwd)

    @pytest.fixture(scope="class")
    def bad_login1(self, request):
        return datacloud.login.CreateLoginAPI(request.cls.dc_host, "bogus_user_name@gmail.com", request.cls.dc_pwd)

    @pytest.fixture(scope="class")
    def bad_login2(self, request):
        return datacloud.login.CreateLoginAPI(request.cls.dc_host, request.cls.dc_user, "bogus_pwd")

    @pytest.fixture(scope="class")
    def bad_login3(self, request):
        return datacloud.login.CreateLoginAPI(request.cls.dc_host, "bogus_user_name@gmail.com", "bogus_pwd")

    def test_login1(self, good_login):
        logging.info("Test login response message")
        expect_value = "Login successful"
        actual_value = good_login.get_message()
        err_msg = "Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login2(self, good_login):
        logging.info("Test login response status")
        expect_value = True
        actual_value = good_login.get_success_status()
        err_msg = "Did not get a success true outcome - Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login3(self, good_login):
        logging.info("Test login user id is correct.")
        expect_value = 21610
        actual_value = good_login.get_userid()
        err_msg = "Did not get correct user id - Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login4(self, good_login):
        logging.info("Test login account id is correct.")
        expect_value = 1193
        actual_value = good_login.get_accountid()
        err_msg = "Did not get correct account id - Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login5(self, good_login):
        logging.info("Test login account external id is correct.")
        expect_value = "Actian QA Stage"
        actual_value = good_login.get_accountexternalid()
        err_msg = "Did not get correct external account id - Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login6(self, bad_login1):
        logging.info("Test we can not log into the DataCloud Integration Manager console with bogus username.")
        expect_value = "DX_EXCEPTION: INVALID_SESSION: Login failed; Invalid user or password"
        actual_value = bad_login1.get_error()
        err_msg = "Did not get expected error message: - Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

    def test_login7(self, bad_login2):
        logging.info("Test we can not log into the DataCloud Integration Manager console with bogus password.")
        expect_value = "DX_EXCEPTION: INVALID_SESSION: Login failed; Invalid user or password"
        actual_value = bad_login2.get_error()
        err_msg = "Did not get expected error message: - Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

