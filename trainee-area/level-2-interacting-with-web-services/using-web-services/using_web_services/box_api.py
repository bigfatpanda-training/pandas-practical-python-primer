"""
This module will interact with the Box API and demonstrate how to integrate
with OAUTH2 based APIs - the current standard in Web Services.
"""
import json

import boxsdk
from configuration_panda import ConfigurationPanda

program_settings = ConfigurationPanda()


if __name__ == "__main__":

    oauth = boxsdk.OAuth2(
        client_id=program_settings['credentials']['clientId'],
        client_secret=program_settings['credentials']['clientSecret'],
        access_token=program_settings['credentials']['developerToken'])

    box_client = boxsdk.Client(oauth)

    # Obtain Box User Info
    box_user_info = box_client.user(user_id='me').get()

    # Obtain Root Folder Handle and Info
    root_folder = box_client.folder(folder_id='0').get()

    # Root Folder Items
    items = box_client.folder(folder_id='0').get_items(limit=100, offset=0)

    for item in items:
        if item.type == "file":
            api_response = json.loads(
                box_client.file(file_id=item.id).get().content().decode())
            print("-" * 50)
            print("File Name: {}".format(item.name))
            print("File Content: {}".format(api_response['atext']['text']))