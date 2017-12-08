"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module enables getting the package entry points.
         URL: https://dxapistage.actiandatacloud.com/v2/jobtemplates/{jobtemplate_id}/package/entrypoints
      METHOD: GET
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = GetEntryPointsAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "JobTemplateId"
                               )

print(response.get_entrypoints())

"""

import json
import requests


class GetEntryPointsAPI(object):
    """Builds up an RESTful endpoint to Get Entry Points related to a package"""
    def __init__(self, host, token, jobtemplateid=None):

        # Complete URL
        self.host = host
        self.jobtemplateid = jobtemplateid
        self.endpoint = "https://" + self.host + "/v2/jobtemplates/" + self.jobtemplateid + "/package/entrypoints"

        # Create JobTemplate Request
        self.token = token
        header_info = {"authorization": str(self.token)}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_entrypoints_response(self):
        """Gets the entire response from /package/entrypoints."""
        return self.response_json

    def get_packagename(self):
        """Gets the package name for a job template"""
        return self.response_json["packageName"]

    def get_map_entrypoint(self):
        """Gets the entry point related to a map."""
        return self.response_json["entrypoints"][0]

    def get_process_entrypoint(self):
        """Gets entry point related to a process"""
        return self.response_json["entrypoints"][1]
