"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module sends a job for execution.
         URL: https://dxapistage.actiandatacloud.com/v2/jobconfigs/{config Id}/jobs
      METHOD: POST
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = PostJobExecutionAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "Config_Id"
                               )

print(response.get_jobexecution_msg())

"""

import json
import requests


class PostJobExecutionAPI(object):
    """Builds up an RESTful endpoint to Execute a job configuration"""
    def __init__(self, host, token, config_id=None):

        # Complete URL
        self.host = host
        self.config_id = config_id
        self.endpoint = "https://" + self.host + "/v2/jobconfigs/" + self.config_id + "/jobs"

        # Run Job Configuration
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.post(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_jobexecution_msg(self):
        """Get the response of Job Execution API"""
        return self.response_json
