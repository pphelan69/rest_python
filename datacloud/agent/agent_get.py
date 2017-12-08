import json
import requests


class GetAgentAPI(object):

    def __init__(self, host, token, size=None):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/agents?"

        # URL part 2 (i.e. parameters )
        self.size = size
        url_param1 = "size=" + self.size + "&" if self.size is not None else ""

        url_part2 = url_param1

        # Complete URL
        self.endpoint = url_part1 + url_part2
        # print(self.endpoint)

        # Setup Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_agent_deviceid(self, agenthost):
        resp = self.response_json
        for i in range(0, len(resp["items"])):
            if resp["items"][i]["serverHostname"] == agenthost:
                return resp["items"][i]["deviceId"]
        return ""

    def get_agent_list(self):
        agent_list = []
        resp = self.response_json
        for i in range(0, len(resp["items"])):
            agent_list.append(resp["items"][i]["serverHostname"])

        return agent_list
