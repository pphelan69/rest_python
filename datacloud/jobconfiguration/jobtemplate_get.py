"""
This module tests the GET api: https://dxapistage.actiandatacloud.com/v2/jobtemplates/{id}

It gets the template details for a template by template id

Here is how you would call the api and use associated methods:

x = GetTemplateAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                   "36a10010-c719-4be2-980c-8a3794165194")
print(x.get_jobtemplate_name())
print(x.get_jobtemplate_id())
print(x.get_jobtemplate_id_by_name())
print(x.get_jobtemplate_by_id())

"""

import json
import logging
import requests


class GetTemplateAPI(object):
    """Builds up an RESTful endpoint to Get info on a template based on template id."""
    def __init__(self, host, token, jobtemplateid=None, size=None):

        # URL part 1
        self.host = host
        url_part1 = "https://" + self.host + "/v2/jobtemplates"

        # URL part 2 (i.e. parameters )
        self.size = size
        self.jobtemplateid = jobtemplateid
        url_param1 = "?size=" + self.size + "&" if self.size is not None else ""
        url_param2 = "/" + self.jobtemplateid if self.jobtemplateid is not None else ""

        url_part2 = url_param1 + url_param2

        # Complete URL
        self.endpoint = url_part1 + url_part2
        # print(self.endpoint)

        # Setup Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.get(self.endpoint, headers=header_info)

        # Get JSON Response
        self.response_json = json.loads(resp.text)
        logging.info(self.response_json)

    def get_jobtemplate_name(self):
        """Get the name of a particular Jobtemplate."""
        return self.response_json["items"][0]["name"]

    def get_jobtemplate_id(self):
        """Get the Id of a particular Jobtemplate."""
        return self.response_json["items"]["id"]

    def get_jobtemplate_id_by_name(self):
        """Get the Id of a jobtemplate by its Name"""
        resp = self.response_json
        for i in range(0, len(resp["items"])):
            if resp["items"][i]["name"] == "AUTO_TEMPLATE":
                return resp["items"][i]["id"]
        return ""

    def get_jobtemplate_by_id(self):
        """Get a Single Template based on its Id"""
        return self.response_json
