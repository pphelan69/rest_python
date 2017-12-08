"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This is a E2E scenario which tests the features like
       Template Creation, Package File Upload, Package and Entry Point selection
       Macro Creation and Job Execution.
"""

import logging
import pytest
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=-1)
class TestScenario1(BaseTest):

    def test_scenario1(self, create_jobtemplate, delete_jobtemplate):

        # [Step:1 Creating a Job Template]
        logging.info("Creating a Job Template")
        expect_value = "JobTemplate created"
        actual_value = create_jobtemplate.get_jobtemplate_msg()
        err_msg = "Job Template Creation Failed: Expected: " + str(expect_value) + " got: " + actual_value
        self.log_assert(actual_value == expect_value, err_msg)

        # <todo Adding more scenario steps here>

        # [Step:2 Deleting a Job Template]
        logging.info("Deleting a Job Template")
        expect_value = 204
        actual_value = delete_jobtemplate.get_delete_status()
        err_msg = "Job Template Deletion Failed: Expected Status: " + str(expect_value) + " got: " + str(actual_value)
        self.log_assert(actual_value == expect_value, err_msg)
