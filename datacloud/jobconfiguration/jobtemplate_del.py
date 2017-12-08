"""
This module tests the DELETE api: https://dxapistage.actiandatacloud.com/v2/jobtemplates/{id}

It deletes the template based on the template id

Here is how you would call the api and use associated methods:

x = DeleteTemplateAPI("dxapistage.actiandatacloud.com",
                   "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                   "36a10010-c719-4be2-980c-8a3794165194")
print(x.get_delete_status())
"""

import requests


class DeleteTemplateAPI(object):
    """Builds up an RESTful endpoint to Delete a template based on template id."""
    def __init__(self, host, token, template_id=None):
        # URL part 1
        self.host = host
        self.template_id = template_id

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/jobtemplates/" + self.template_id

        # Delete JobTemplate Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.delete(self.endpoint, headers=header_info)

        # Get Response Status
        self.status = resp.status_code

    def get_delete_status(self):
        """Gets the Status code returned after service call."""
        return self.status
