import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=2)
class TestPostTemplateFilesAPI(BaseTest):

    def test_postpackage_files1(self, post_jobtemplate_files):
        logging.info("Added the PackageFile to the Template")
        logging.info(post_jobtemplate_files.add_package_files())

