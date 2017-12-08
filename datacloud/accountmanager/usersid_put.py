""" This module tests the put api: https://dxapistage.actiandatacloud.com/v2/user/{id}

This api is used to update the username and/or password for a particular user as determined by his/her user id

Here is how you would call the api and use associated methods:

x = UpdateUserIDAPI("dxapistage.actiandatacloud.com", "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
"21611", {"username": "pphelan69@gmail.com","password": "Actian12345$"})
print(x.get_msg())

"""
import json
import requests


class UpdateUserIDAPI(object):
    """Builds up an endpoint to get info on a user based on user id."""

    def __init__(self, host, token, user_id, payload=None):

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

        # CreateJobTemplate payload
        self.postdata = json.dumps(payload)

        # Setup Request
        self.token = token
        header_info = {'authorization': str(self.token), 'content-type': 'application/json'}
        resp = requests.put(self.endpoint, data=self.postdata, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_msg(self):
        """Get the username for a particular user."""
        return self.response_json["message"]

