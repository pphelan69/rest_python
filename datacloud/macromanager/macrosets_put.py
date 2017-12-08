""" This module tests the put api: https://dxapistage.actiandatacloud.com/v1/macrosets/{user_id}/macros/{macro_name}

This api is used to update the macro values for a particular macro.

Here is how you would call the api:

x = UpdateMacroSetAPI("dxapistage.actiandatacloud.com",
                      "21611",
                      "mymacro",
                      "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                      "1193"
                      {"name": "log_dir", "value": "C:/data/logs", "secure": False})


notes:
 - "dxapistage.actiandatacloud.com" is server which hosts the rest api
 - "21611" is the user id
 - "mymacro" is the target macro.
 - "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi" is the token and is part of the request header
 - "1193" is the Account ID and is part of the Request header.
 - {name: "log_dir", value: "C:/data/logs", secure: false} is the request payload.


__author__ = "Peter Phelan"
__email__ = "peter.phelan@actian.com"

"""

import json
import requests


class UpdateMacroSetAPI(object):
    """Builds up an endpoint to get info on a user based on user id.


    """

    def __init__(self, host, user_id, macro_name, token, account_id, payload=None):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v1/macrosets"

        # URL part 2 (i.e. parameters )
        self.user_id = user_id   # User Id
        url_param1 = "/" + self.user_id

        self.macro_name = macro_name   # Macro name
        url_param2 = "/macros/" + self.macro_name

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
        resp = requests.put(self.endpoint, headers=header_info, data=self.putdata, )

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

        # print(self.response_json)

    def get_success(self):
        """Returns True if the maco update is a success or False if not a success."""
        return self.response_json["success"]

    def get_name(self):
        """Get the name of the macro."""
        return self.response_json["name"]

    def get_msg(self):
        """Get the response message after a macro update call."""
        return self.response_json["message"]
