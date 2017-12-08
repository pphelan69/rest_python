import logging
import re

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=1)
class TestCreateJobTemplate(BaseTest):

    def test_createjob_template1(self, create_jobtemplate):
        logging.info("Testing that JobTemplate Creation Msg wad Received in the Response")
        expect_value = "JobTemplate created"
        actual_value = create_jobtemplate.get_jobtemplate_msg()
        err_msg = "Job Template Creation Failed: Expected: " + str(expect_value) + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

    def test_createjob_template2(self, create_jobtemplate):
        logging.info("Testing that the Correct JobTemplate Creation status was received in the Response")
        expect_value = True
        actual_value = create_jobtemplate.get_jobtemplate_status()
        err_msg = "Job Template Creation Failed: Expected: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)

    def test_createjob_template3(self, create_jobtemplate):
        logging.info("Testing that the Response Contains a JobTemplate Id")
        expected_jobtemplateid = re.findall("(^[a-zA-Z0-9._-]+$)", create_jobtemplate.get_jobtemplate_id())
        actual_jobtemplateid = create_jobtemplate.get_jobtemplate_id()
        if expected_jobtemplateid:
            for item in expected_jobtemplateid:
                actual = item in actual_jobtemplateid
                expected = True
                self.log_assert(actual == expected, "Job Template Id not Created")

    def test_createjob_template4(self, create_jobtemplate):
        logging.info("Testing that the Correct Link to the Created Job Template ID was Created in the Response")
        logging.info(create_jobtemplate.get_jobtemplate_byid())
        expect_value = "https://dxapistage.actiandatacloud.com/v2/jobtemplates/" + \
                       create_jobtemplate.get_jobtemplate_id()
        actual_value = create_jobtemplate.get_jobtemplate_byid()
        err_msg = "Expected: " + expect_value + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)
