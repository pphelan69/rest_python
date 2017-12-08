""" This module tests the delete api: https://dxapistage.actiandatacloud.com/v1/macrosets/{user_id}/macros/{macro_name}

This api is used to delete a macro

Here is how you would call the api:

x = DeleteMacroSetAPI("dxapistage.actiandatacloud.com",
                      "21611",
                      "mymacro",
                      "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                      "1193")


notes:
 - "dxapistage.actiandatacloud.com" is server which hosts the rest api
 - "21610" is the user id
 - "mymacro" is the target macro.
 - "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi" is the token and is part of the request header
 - "1193" is the Account ID and is part of the Request header.

__author__ = "Peter Phelan"
__email__ = "peter.phelan@actian.com"


"""

import requests


class DeleteMacroSetAPI(object):
    """Builds up an endpoint to get info on a user based on user id.


    """

    def __init__(self, host, user_id, macro_name, token, account_id):

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

        # Send the Put request
        resp = requests.delete(self.endpoint, headers=header_info)
        # print(self.endpoint)

        # Get JSON Response
        self.response_text = resp.text
        # self.response_json = json.loads(response_text)

    def delete_status(self):
        return self.response_text
