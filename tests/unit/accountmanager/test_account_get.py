import logging
import pytest
import datacloud.accountmanager
from tests.base_test import BaseTest


"""
We are basically testing we get this json response when using the get api:
https://{host}/v2/account


{
    "active": true,
    "created": "2014-11-10T10:41:55.190-06:00",
    "createdByUser": {
        "id": "1",
        "name": "systemuser",
        "links": {
            "self": "https://dxapistage.actiandatacloud.com/v2/users/1"
        }
    },
    "externalId": "Actian QA Stage",
    "id": 1193,
    "lastModified": "2014-11-10T10:43:14.493-06:00",
    "lastModifiedByUser": {
        "id": "1",
        "name": "systemuser",
        "links": {
            "self": "https://dxapistage.actiandatacloud.com/v2/users/1"
        }
    },
    "name": "Actian QA Stage"
}
"""


@pytest.mark.usefixtures("setup")
class TestGetAccounts(BaseTest):

    @pytest.fixture(scope="class")
    def account_fixture1(self, request):
        my_account = datacloud.accountmanager.GetAccountAPI(request.cls.dc_host, request.cls.dc_token)
        logging.info("In account_fixture1")
        return my_account

    def test_account_test1(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - name")

        expect_value = "Actian QA Stage"
        actual_value = account_fixture1.get_name()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_account_test2(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - createdByUser:name")

        expect_value = "systemuser"
        actual_value = account_fixture1.get_createdbyuser_name()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_account_test3(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - createdByUser:id")

        expect_value = "1"
        actual_value = account_fixture1.get_createdbyuser_id()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_account_test4(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - externalId")

        expect_value = "Actian QA Stage"
        actual_value = account_fixture1.get_externalid()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_account_test5(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - id")

        expect_value = 1193
        actual_value = account_fixture1.get_id()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_account_test6(self, account_fixture1):
        logging.info("Unit Testing: /v2/account get api response - active")

        expect_value = True
        actual_value = account_fixture1.is_active()
        err_msg = "Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)


