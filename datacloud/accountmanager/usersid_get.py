""" This module tests the get api: https://dxapistage.actiandatacloud.com/v2/user/{id}

Here is how you would call the api and use associated methods:

x = GetUserIDAPI("dxapistage.actiandatacloud.com",
                 "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi","21610")
print(x.get_user_name())
print(x.get_creation_datetime())
print(x.get_lastmodified_datetime())
print(x.get_user_external_id())
print(x.get_user_id())
print(x.is_active())
print(x.is_admin())
print(x.get_user_account_id())
print(x.get_user_account_name())
print(x.get_last_modifiedbyuser_id())
print(x.get_last_modifiedbyuser_name())

"""
import json
import requests


class GetUserIDAPI(object):
    """Builds up an endpoint to get info on a user based on user id."""
    def __init__(self, host, token, user_id):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/users"

        # URL part 2 (i.e. parameters )
        self.user_id = user_id
        url_param1 = "/" + self.user_id

        url_part2 = url_param1

        # Complete URL
        self.endpoint = url_part1 + url_part2
        # print(self.endpoint)

        # Setup Request
        self.token = token
        header_info = {'authorization': str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_creation_datetime(self):
        """returns the date and time when the user was first created."""
        return self.response_json["created"]

    def get_lastmodified_datetime(self):
        """returns the date and time when the user was last modified."""
        return self.response_json["lastModified"]

    def get_last_modifiedbyuser_id(self):
        """returns the user id of the user who last modified the user."""
        return self.response_json["lastModifiedByUser"]["id"]

    def get_last_modifiedbyuser_name(self):
        """returns the user name of the user who last modified the user."""
        return self.response_json["lastModifiedByUser"]["name"]

    def get_user_name(self):
        """returns the username."""
        return self.response_json["username"]

    def get_user_id(self):
        """returns the user id."""
        return self.response_json["id"]

    def get_user_external_id(self):
        """returns the user id."""
        return self.response_json["externalId"]

    def get_user_account_id(self):
        """returns the users associated account id."""
        return self.response_json["account"]["id"]

    def get_user_account_name(self):
        """returns the users associated account name."""
        return self.response_json["account"]["name"]

    def is_active(self):
        """returns True if user is active, otherwise returns False"""
        return self.response_json["active"]

    def is_admin(self):
        """returns True if user is an admin, otherwise returns False"""
        return self.response_json["admin"]
