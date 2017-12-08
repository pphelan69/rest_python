import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestGetJobTemplate(BaseTest):

    def test_createjob_template1(self, get_jobtemplate):
        logging.info("All Job Templates")
        logging.info(get_jobtemplate.get_jobtemplate_id_by_name())

    def test_createjob_template2(self, get_jobtemplate_byid):
        logging.info("Get Job Template By ID")
        logging.info(get_jobtemplate_byid.get_jobtemplate_by_id())
