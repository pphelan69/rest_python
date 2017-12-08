import json
import requests


class GetAccountAPI(object):

    def __init__(self, host, token):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/account"

        # Complete URL
        self.endpoint = url_part1

        # Setup Request
        self.token = token
        header_info = {'authorization': str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def is_active(self):
        """returns True if account is active, otherwise returns False"""
        return self.response_json["active"]

    def get_creation_datetime(self):
        """returns the date and time when the account was first created."""
        return self.response_json["created"]

    def get_createdbyuser_id(self):
        """returns the user id of the user who last modified the account."""
        return self.response_json["createdByUser"]["id"]

    def get_createdbyuser_name(self):
        """returns the name of the user who last modified the account."""
        return self.response_json["createdByUser"]["name"]

    def get_externalid(self):
        """returns the account external id."""
        return self.response_json["externalId"]

    def get_id(self):
        """returns the account id."""
        return self.response_json["id"]

    def get_lastmodified_datetime(self):
        """returns the date and time when the account was last modified."""
        return self.response_json["lastModified"]

    def get_last_modifiedbyuser_id(self):
        """returns the user id of the user who last modified the account."""
        return self.response_json["lastModifiedByUser"]["id"]

    def get_last_modifiedbyuser_name(self):
        """returns the name of the user who last modified the account."""
        return self.response_json["lastModifiedByUser"]["name"]

    def get_name(self):
        """returns the account name."""
        return self.response_json["name"]

