"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module enables creating a new job config for a template.
         URL: https://dxapistage.actiandatacloud.com/v2/jobconfigs
      METHOD: POST
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = CreateConfigAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "JSON Payload"
                               )

print(response.get_jobconfig_msg())
print(response.get_jobconfig_status())
print(response.get_jobconfig_id())
print(response.get_jobconfig_byid())

"""


import json
import requests
from miscutils import file_utils


class CreateConfigAPI(object):
    """Builds up an RESTful endpoint to Create a Config."""
    def __init__(self, host, token, data=None):

        # URL part 1
        self.host = host

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/jobconfigs"

        # CreateJobTemplate payload
        self.postdata = json.dumps(data)

        # Create JobTemplate Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.post(self.endpoint, data=self.postdata, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

        # Write Response to a JSON File
        mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobconfig.json"
        with open(mypath, 'w')as outfile:
            json.dump(self.response_json, outfile)

    def get_jobconfig_msg(self):
        """Gets the message from response after config creation."""
        return self.response_json["message"]

    def get_jobconfig_status(self):
        """Gets the boolean response after a successful config creation."""
        return self.response_json["success"]

    def get_jobconfig_id(self):
        """Gets the Template Id from response after a successful config creation."""
        return self.response_json["id"]

    def get_jobconfig_byid(self):
        """Gets the href for the newly created config."""
        return self.response_json["links"]["self"]
