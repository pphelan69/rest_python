"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module enables getting the package files of a template
         URL: https://dxapistage.actiandatacloud.com/v2/jobtemplates/{jobtemplate_id}/files
      METHOD: GET
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = GetTemplateFilesAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "JobTemplateId"
                               )

print(response.get_template_files())

"""


import json
import requests


class GetTemplateFilesAPI(object):
    """Builds up an REST full endpoint to Get files related to a job template"""
    def __init__(self, host, token, jobtemplateid=None):

        # Complete URL
        self.host = host
        self.jobtemplateid = jobtemplateid
        self.endpoint = "https://" + self.host + "/v2/jobtemplates/" + self.jobtemplateid + "/files"

        # Create JobTemplate Request
        self.token = token
        header_info = {"authorization": str(self.token)}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_template_files(self):
        """Gets all the files associated with a job template."""
        return self.response_json
