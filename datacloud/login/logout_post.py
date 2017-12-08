"""
This module tests the POST api: https://dxapistage.actiandatacloud.com/v2/logout

It Deletes an existing session and logout a user.

Here is how you would call the api and use associated methods:

x = LogoutAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi")
print(x.get_logout_msg())
print(x.get_logout_errmsg())
"""


import json
import requests


class CreateLogoutAPI(object):
    """Builds up an RESTful endpoint to Logout a DC_X User"""
    def __init__(self, host, token):

        self.host = host

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/logout"

        # Logout Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.post(self.endpoint, headers=header_info)

        # Get JSON Response
        self.response_json = json.loads(resp.text)

    def get_logout_msg(self):
        """Gets the success message after logout"""
        return self.response_json["success"]

    def get_logout_errmsg(self):
        """Gets the errors on a unsuccessful logout"""
        return self.response_json["error"]
