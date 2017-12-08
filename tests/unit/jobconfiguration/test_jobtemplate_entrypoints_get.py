import logging

import pytest

from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup")
@pytest.mark.run(order=6)
class TestGetEntryPointsAPI(BaseTest):

    def test_getentrypoint_files1(self, get_package_entrypoints):
        logging.info("Entry Points for the package file are")
        logging.info(get_package_entrypoints.get_entrypoints_response())

    def test_getentrypoint_files2(self, get_package_entrypoints):
        logging.info("Package name for the template")
        logging.info(get_package_entrypoints.get_packagename())

    def test_getentrypoint_files3(self, get_package_entrypoints):
        logging.info("Map Entry Point for the package file")
        logging.info(get_package_entrypoints.get_map_entrypoint())

    def test_getentrypoint_files4(self, get_package_entrypoints):
        logging.info("Process Entry Point for the package file")
        logging.info(get_package_entrypoints.get_process_entrypoint())
