import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=3)
class TestGetJobTemplate(BaseTest):

    def test_putjob_template1(self, update_jobtemplate):
        logging.info("Update a Job Template")
        logging.info(update_jobtemplate.get_updated_jobtemplate())
