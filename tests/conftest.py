
from tests.fixtures.jobconfiguration import *


@pytest.fixture(scope="class")
def setup(request):

    # Get all configuration variables from json file
    mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/datacloud.json"
    logging.info(mypath)
    with open(mypath) as config_file:
        config = json.load(config_file)

    # Read all json config variables
    dc_host = config[0]["dx"]["host"]
    dc_user = config[0]["dx"]["user"]
    dc_pwd = config[0]["dx"]["password"]
    dc_agent1 = config[0]["agents"]["agent1"]

    dc_account1_id = config[0]["account1"]["id"]
    dc_account1_name = config[0]["account1"]["name"]
    dc_usersid_1 = config[0]["user1"]["id"]
    dc_usersname_1 = config[0]["user1"]["username"]
    dc_usersid_2 = config[0]["user2"]["id"]
    dc_usersname_2 = config[0]["user2"]["username"]

    # Authentication - Get a login request bearer token, which is needed by all rest calls in the request header
    dc_session = datacloud.login.CreateLoginAPI(dc_host, dc_user, dc_pwd)
    dc_token = str(dc_session.get_token())

    # Expose the request bearer token and all json config variable to test classes:
    request.cls.dc_token = dc_token
    request.cls.dc_host = dc_host
    request.cls.dc_user = dc_user
    request.cls.dc_pwd = dc_pwd
    request.cls.dc_agent1 = dc_agent1
    request.cls.dc_account1_id = dc_account1_id
    request.cls.dc_account1_name = dc_account1_name
    request.cls.dc_usersid_1 = dc_usersid_1
    request.cls.dc_usersname_1 = dc_usersname_1
    request.cls.dc_usersid_2 = dc_usersid_2
    request.cls.dc_usersname_2 = dc_usersname_2



