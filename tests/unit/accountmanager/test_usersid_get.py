import logging
import datacloud.accountmanager
import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestGetUserID(BaseTest):

    @pytest.fixture(scope="class")
    def userid_fixture1(self, request):
        userid = datacloud.accountmanager.GetUserIDAPI(request.cls.dc_host, request.cls.dc_token,
                                                       request.cls.dc_usersid_2)
        return userid

    def test_usersid_get1(self, userid_fixture1):
        logging.info("Unit Testing: /v2/users/{user_id} get api response - username")

        expect_value = "pphelan69@gmail.com"
        actual_value = userid_fixture1.get_user_name()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

