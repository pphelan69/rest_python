""" This module tests the get api: https://dxapistage.actiandatacloud.com/v1/macrosets?includeMacros=true

This api is used to show all the macro's associated with an account.

Here is how you would call the api:

x = GetMacroSetAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                   "1193")


notes:
 - "dxapistage.actiandatacloud.com" is server which hosts the rest api
 - "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi" is the token and is part of the request header
 - "1193" is the Account ID and is part of the Request header.

__author__ = "Peter Phelan"
__email__ = "peter.phelan@actian.com"

"""

import json
import requests


class GetMacroSetAPI(object):
    """Tests the rest api:
    https://dxapistage.actiandatacloud.com/v1/macrosets?includeMacros=true


    """

    def __init__(self, host, token, account_id):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v1/macrosets?"

        # URL part 2 (i.e. parameters )
        url_param1 = "includeMacros=true"
        url_param2 = "size=500"

        url_part2 = url_param1 + "&" + url_param2

        # Complete URL
        self.endpoint = url_part1 + url_part2
        # print(self.endpoint)

        # Setup Request Header
        self.token = token
        self.account_id = account_id
        header_info = {'authorization': str(self.token), 'accountid': self.account_id,
                       'content-type': 'application/json'}

        # Send the Put request
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_all_macro_names(self):
        macros = []
        num_macros = len(self.response_json["macrosets"])

        for i in range(0, num_macros):
            if self.response_json["macrosets"][i]["macros"]:
                for j in range(0, len(self.response_json["macrosets"][i]["macros"])):
                    macros.append(self.response_json["macrosets"][i]["macros"][j]["name"])

        return macros

    def get_macro_value(self, macro_name):
        num_macros = len(self.response_json["macrosets"])

        for i in range(0, num_macros):
            if self.response_json["macrosets"][i]["macros"]:
                for j in range(0, len(self.response_json["macrosets"][i]["macros"])):
                    if self.response_json["macrosets"][i]["macros"][j]["name"] == macro_name:
                        return self.response_json["macrosets"][i]["macros"][j]["value"]
        return ""

    def get_macro_macroset(self, macro_name):
        num_macros = len(self.response_json["macrosets"])

        for i in range(0, num_macros):
            if self.response_json["macrosets"][i]["macros"]:
                for j in range(0, len(self.response_json["macrosets"][i]["macros"])):
                    if self.response_json["macrosets"][i]["macros"][j]["name"] == macro_name:
                        return self.response_json["macrosets"][i]["macros"][j]["macroset"]
        return ""

    def is_macro_secure(self, macro_name):
        num_macros = len(self.response_json["macrosets"])

        for i in range(0, num_macros):
            if self.response_json["macrosets"][i]["macros"]:
                for j in range(0, len(self.response_json["macrosets"][i]["macros"])):
                    if self.response_json["macrosets"][i]["macros"][j]["name"] == macro_name:
                        return self.response_json["macrosets"][i]["macros"][j]["secure"]
        return None
