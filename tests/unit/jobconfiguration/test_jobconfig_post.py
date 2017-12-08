import logging
import pytest
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=4)
class TestCreateConfigAPI(BaseTest):

    def test_create_config1(self, create_jobconfig):
        logging.info("Created Job Config for a Template")
        logging.info(create_jobconfig.get_jobconfig_msg())

