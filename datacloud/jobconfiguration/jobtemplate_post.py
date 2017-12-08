"""
This module tests the POST api: https://dxapistage.actiandatacloud.com/v2/jobtemplates

It Creates a template with the given name.

Here is how you would call the api and use associated methods:

x = CreateTemplateAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                   "Pass Request payload here")
print(x.get_jobtemplate_msg())
print(x.get_jobtemplate_status())
print(x.get_jobtemplate_id())
print(x.get_jobtemplate_byid())

"""


import json
import requests
from miscutils import file_utils


class CreateTemplateAPI(object):
    """Builds up an RESTful endpoint to Create a template."""
    def __init__(self, host, token, data=None):

        # URL part 1
        self.host = host

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/jobtemplates"

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
        mypath = file_utils.get_auto_loc_root() + "/dc_integ_auto/config/payloads/jobtemplate.json"
        with open(mypath, 'w')as outfile:
            json.dump(self.response_json, outfile)

    def get_jobtemplate_msg(self):
        """Gets the message from response after jobtemplate creation."""
        return self.response_json["message"]

    def get_jobtemplate_status(self):
        """Gets the boolean response after a successful template creation."""
        return self.response_json["success"]

    def get_jobtemplate_id(self):
        """Gets the Template Id from response after a successful template creation."""
        return self.response_json["id"]

    def get_jobtemplate_byid(self):
        """Gets the href for the newly created template."""
        return self.response_json["links"]["self"]
