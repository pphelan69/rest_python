import logging
import pytest
import datacloud.accountmanager
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestGetUsers(BaseTest):

    @pytest.fixture(scope="class")
    def users_fixture1(self, request):
        users = datacloud.accountmanager.GetUsersAPI(request.cls.dc_host, request.cls.dc_token)
        logging.info("In users_fixture1")
        return users

    def test_users_test1(self, users_fixture1):
        logging.info("Unit Testing: /v2/users get api response - username")

        expect_value = True
        actual_value = "peter.phelan@actian.com" in users_fixture1.get_all_usernames()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
