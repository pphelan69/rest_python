import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=-2)
class TestDeleteJobTemplate(BaseTest):

    def test_jobtemplate_delete1(self, delete_jobtemplate):
        logging.info("Testing that JobTemplate Deletion is Successful")
        logging.info(delete_jobtemplate.get_delete_status())
