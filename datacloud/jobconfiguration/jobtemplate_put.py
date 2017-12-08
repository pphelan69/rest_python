"""
This module tests the PUT api: https://dxapistage.actiandatacloud.com/v2/jobtemplates

It Replaces a template with the given changes.
It keeps the same resource id but updates the meta data.

Here is how you would call the api and use associated methods:

x = PutTemplateAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                   "Pass Request payload here","36a10010-c719-4be2-980c-8a3794165194")
print(x.get_updated_jobtemplate())
"""


import json
import logging
import requests


class UpdateTemplateAPI(object):
    """Builds up an RESTful endpoint to Update a template."""
    def __init__(self, host, token, data=None, jobtemplateid=None):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/jobtemplates"

        # URL part 2 (i.e. parameters )
        self.jobtemplateid = jobtemplateid
        url_param1 = "/" + self.jobtemplateid if self.jobtemplateid is not None else ""

        url_part2 = url_param1

        # Complete URL
        self.endpoint = url_part1 + url_part2
        logging.info(self.endpoint)

        # CreateJobTemplate payload
        self.putdata = json.dumps(data)
        logging.info(self.putdata)

        # Create JobTemplate Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.put(self.endpoint, data=self.putdata, headers=header_info)

        # Get JSON Response
        response_text = resp.text
        self.response_json = json.loads(response_text)

    def get_updated_jobtemplate(self):
        """Gets the Updated job template right now changes from active to inactive."""
        return self.response_json
