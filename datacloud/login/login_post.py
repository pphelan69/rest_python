import json
import base64
import requests


class CreateLoginAPI(object):

    def __init__(self, host, user, password):
        # Build up endpoint URL
        self.host = host
        self.user = user
        self.password = password
        self.endpoint = "https://" + self.host + "/v2/login"

        # Login payload
        postdata = {"username": self.user, "password": self.password}
        data = json.dumps(postdata)

        # Execute login payload
        self.resp = requests.post(self.endpoint, data=data)
        self.json_data = json.loads(self.resp.text)

    def login(self):
        return self.json_data

    def get_token(self):
        sessionid_value = self.json_data["sessionid"]
        token = "Bearer: " + base64.b64encode(bytes(sessionid_value))
        return token

    def get_sessionid(self):
        return self.json_data["sessionid"]

    def get_message(self):
        return self.json_data["message"]

    def get_success_status(self):
        return self.json_data["success"]

    def get_visitor_key(self):
        return self.json_data["visitorkey"]

    def get_userid(self):
        return self.json_data["userid"]

    def get_accountid(self):
        return self.json_data["accountid"]

    def get_accountexternalid(self):
        return self.json_data["accountexternalid"]

    def get_error(self):
        return self.json_data["error"]
