import logging
import time
from miscutils import file_utils


class BaseTest(object):

    @classmethod
    def setup_class(cls):
        # Setup the logging.
        log_file = file_utils.get_auto_loc_root() + "/dc_integ_auto/logs/DataCloud_" + \
                   time.strftime("%Y%m%d-%H%M%S") + ".log"
        logging.basicConfig(filename=log_file, level=logging.INFO)

    @classmethod
    def teardown_class(cls):
        logging.info("Teardown - Currently no teardown operations")

    @classmethod
    def log_assert(cls, test, msg):
        if not test:
            logging.error(msg)
            assert test, msg
