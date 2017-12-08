import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestGetTemplateFilesAPI(BaseTest):

    def test_getjobtemplate_files1(self, get_jobtemplate_files):
        logging.info("Job Template Files Are")
        logging.info(get_jobtemplate_files.get_template_files())

