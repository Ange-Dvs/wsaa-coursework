import requests
import json
import base64
from config import config as cfg 

apiKey = cfg['githubkey']
repo_owner = 'Ange-Dvs'
repo_name = 'aprivateone'
file_path = 'sample_file_for_assignment04.txt'  # The file path in the repo
file_content = 'This text was generated using ChatGPT to form the baseline for the file to be updated. Andrew had always been a curious child. Ever since he was young, Andrew would spend hours exploring the woods behind his house, searching for hidden treasures. One day, Andrew stumbled upon an old notebook buried beneath a pile of leaves. Inside, Andrew found strange symbols and messages, as if someone had been keeping secrets for years. Determined to uncover the mystery, Andrew spent days deciphering the notes. "Andrew, this could be the greatest discovery of your life," he muttered to himself. But Andrew realized that the final page was missing. Frustrated but not discouraged, Andrew turned to his best friend, who laughed and said, "Andrew, you always find yourself in the weirdest situations!" Together, they embarked on a mission to solve the mystery, that would lead them to the truth.' 

encoded_content = base64.b64encode(file_content.encode()).decode() # encoding the file content set in the variable above in Base64 format as this is required for GitHub when using the API. .encode() converts the text of the file to bytes, base64.b64encode() converts the bytes to Base64 format, decode() then conversts the base64 bytes into a string which is needed from the API 

url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}' # forming the url using the varibales defined to make it easier to reuse the code

headers = {'Authorization': f'token {apiKey}'} # defining the headers as GitHub requires the key to be passed to modify the repo and indicate the person pushing is authenticated to edit the repo

data = { # structuring the data to be passed
    'message': 'Creating a new file via API', # Commit message to be shown in GitHub for the creation of the file
    'content': encoded_content, # passing the encoded payload of the message 
    'branch': 'main'  # specifying the branch to be called
}

response = requests.put(url, headers=headers, data=json.dumps(data)) # sending the request, the authorization key is passed here in the request

if response.status_code in [200, 201]: # handling the response so that we can see if the creation of the call has been successful 
    print(f'Successfully created/updated {file_path} in repo')
else:
    print(f'Error: {response.status_code} - {response.json()}')
