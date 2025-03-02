# assignment04-github.py
# Thsi program reads a file from a repository and replace all the instances of the text 'Andrew' with my name. 
# The program then commits the changes and pushes the file back to the repository.
# If unexpected response is received for the calls i.e. not 200 or 200/201 depending on the call the error will be returned to the user.

# Author: Angela Davis

import requests
import json
import base64
from config import config as cfg 

apiKey = cfg['githubkey'] # getting private key from config file
repo_owner = 'Ange-Dvs'
repo_name = 'aprivateone'
file_path = 'sample_file_for_assignment04.txt' 
branch = 'main'
my_name = 'Angela'

file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
headers = {'Authorization': f'token {apiKey}'}

response = requests.get(file_url, headers=headers) # reading the orginal file from GitHub

if response.status_code == 200: # checking if reading of file was successful
    file_data = response.json()
    sha = file_data['sha']  # storing the file's SHA hash as this is needed for updating the file
    
    # Decoding the payload, replacing the Andrew text and base64 encoding the updated response
    file_content = base64.b64decode(file_data['content']).decode()
    updated_content = file_content.replace('Andrew', my_name)
    encoded_content = base64.b64encode(updated_content.encode()).decode()

    # Creating the updated payload and running the call to update it using .put 
    commit_message = f'Updated {file_path}: Replaced "Andrew" with "{my_name}"'
    update_data = {
        'message': commit_message,
        'content': encoded_content,
        'sha': sha,  # SHA hash required to update an existing file
        'branch': branch
    }
    update_response = requests.put(file_url, headers=headers, data=json.dumps(update_data))

    if update_response.status_code in [200, 201]: # checking response to see if the update has been successful and telling the user it was or showing error to user if not successful
        print(f'Successfully updated {file_path} and pushed changes to GitHub')
    else:
        print(f'Error updating file: {update_response.status_code} - {update_response.json()}')

else: # throwing error if the call to read the file was not successful and showing the user
    print(f'Error fetching file: {response.status_code} - {response.json()}')
