import json
import requests


class GetUsersAPI(object):

    def __init__(self, host, token):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/users"

        # Complete URL
        self.endpoint = url_part1

        # Setup Request
        self.token = token
        header_info = {'authorization': str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_all_usernames(self):
        users = []
        num_users = len(self.response_json["items"])

        for i in range(0, num_users):
            users.append(self.response_json["items"][i]["username"])

        return users

