
import json
import requests


class GetJobExecutionAPI(object):
    """Builds up an RESTful endpoint to Execute a job configuration"""
    def __init__(self, host, token, config_id=None):

        # Complete URL
        self.host = host
        self.config_id = config_id
        self.endpoint = "https://" + self.host + "/v2/jobconfigs/" + self.config_id + "/jobs"

        # Run Job Configuration
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_jobexecution_msg(self):
        """Get the response of Job Execution API"""
        return self.response_json
