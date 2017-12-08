import json
import requests


class CreateUserAPI(object):

    def __init__(self, host, token, data=None):

        # URL part 1
        self.host = host

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/users"

        # CreateJobTemplate payload
        self.postdata = json.dumps(data)

        # Create JobTemplate Request
        self.token = token
        header_info = {'authorization': str(self.token), 'content-type': 'application/json'}
        resp = requests.post(self.endpoint, data=self.postdata, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_user_creation_id(self):
        return self.response_json["id"]

    def get_user_creation_msg(self):
        return self.response_json["message"]

    def get_user_creation_success(self):
        return self.response_json["success"]
