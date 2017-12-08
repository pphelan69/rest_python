""" This module tests the post api: https://dxapistage.actiandatacloud.com/v1/macrosets/{user_id}/macros

This api is used to add a new macro and its associated attributes together with values for those attributes.

Here is how you would might call the api:

x = CreateMacroSetAPI("dxapistage.actiandatacloud.com",
                      "21611",
                      "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                      "1193"
                      {name: "mymacro2", value: "C:/data/logs", secure: false})


notes:
 - "dxapistage.actiandatacloud.com" is server which hosts the rest api
 - "21611" is the user id
 - "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi" is the token and is part of the request header
 - "1193" is the Account ID and is part of the request header.
 - {name: "log_dir", value: "C:/data/logs", secure: false} is the request payload.

__author__ = "Peter Phelan"
__email__ = "peter.phelan@actian.com"

"""

import json
import requests


class CreateMacroSetAPI(object):
    """Builds up an endpoint to get info on a user based on user id.


    """

    def __init__(self, host, user_id, token, account_id, payload=None):
        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v1/macrosets"

        # URL part 2 (i.e. parameters )
        self.user_id = user_id  # User Id
        url_param1 = "/" + self.user_id

        url_param2 = "/macros"

        url_part2 = url_param1 + url_param2

        # Complete URL
        self.endpoint = url_part1 + url_part2
        # print(self.endpoint)

        # Setup Request Header
        self.token = token
        self.account_id = account_id
        header_info = {'authorization': str(self.token), 'accountid': self.account_id,
                       'content-type': 'application/json'}

        # Payload
        self.putdata = json.dumps(payload)

        # Send the Put request
        resp = requests.post(self.endpoint, headers=header_info, data=self.putdata, )

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_success(self):
        """Returns True if the maco creation is a success or False if not a success."""
        return self.response_json["success"]

    def get_name(self):
        """Get the name of the macro."""
        if 'name' in self.response_json:
            return self.response_json["name"]

    def get_msg(self):
        """Get the response message after a macro is created."""
        return self.response_json["message"]

    def get_error(self):
        """Get the response message after a macro creation call."""
        return self.response_json["error"]





