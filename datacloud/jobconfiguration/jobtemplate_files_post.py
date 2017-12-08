"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module enables Adding the package files to a template
         URL: https://dxapistage.actiandatacloud.com/v2/jobtemplates/{jobtemplate_id}/files?key={Package filename}
      METHOD: POST
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = PostTemplateFilesAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "JobTemplateId",
                               "package file",
                               "key"
                               )

print(response.add_package_files())

"""

import json
import requests


class CreateTemplateFilesAPI(object):
    """Builds up an RESTful endpoint to upload package .jar files"""
    def __init__(self, host, token, jobtemplateid=None, data=None, key=None):

        # URL part 1 -
        self.host = host
        self.jobtemplateid = jobtemplateid
        url_part1 = "https://" + self.host + "/v2/jobtemplates/" + self.jobtemplateid + "/files"

        # URL part 2 (i.e. parameters )
        self.key = key
        url_param1 = "?key=" + self.key if self.key is not None else "NOT-FOUND"
        url_part2 = url_param1

        # Complete URL
        self.endpoint = url_part1 + url_part2

        # Adding Package File
        self.postdata = data

        # Upload Package File Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/octet-stream'}
        resp = requests.post(self.endpoint, data=self.postdata, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def add_package_files(self):
        """Adds jar files to a job template."""
        return self.response_json
