"""
__author__ = "Atul Dadhich"
__email__ = "atull.dadhich@actian.com"

[INFO]
       Usage: This Module enables deleting a new job config.
         URL: https://dxapistage.actiandatacloud.com/v2/jobconfigs
      METHOD: DELETE
        Note: To try it use sample request.

[SAMPLE REQUEST]

response = DeleteConfigAPI(
                               "dxapistage.actiandatacloud.com",
                               "Bearer: ZTA4MmRlMDYtY2ViMS00YTk3LTg4YTgtNGMxZTc0MGJhMjNi",
                               "Config_Id"
                               )

print(response.del_config_status())

"""


import requests


class DeleteConfigAPI(object):
    """Builds up an RESTful endpoint to Delete a Config based on Config id."""
    def __init__(self, host, token, config_id=None):
        # URL part 1
        self.host = host
        self.config_id = config_id

        # Complete URL
        self.endpoint = "https://" + self.host + "/v2/jobconfigs/" + self.config_id

        # Delete JobConfig Request
        self.token = token
        header_info = {"authorization": str(self.token), 'content-type': 'application/json'}
        resp = requests.delete(self.endpoint, headers=header_info)

        # Get Response Status
        self.status = resp.status_code

    def del_config_status(self):
        """Gets the Status code returned after service call."""
        return self.status
