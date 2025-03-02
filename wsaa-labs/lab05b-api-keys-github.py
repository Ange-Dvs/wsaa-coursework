import requests
import json
from config import config as cfg

apiKey = cfg['githubkey'] 
url = 'https://api.github.com/repos/Ange-Dvs/aprivateone' 

response = requests.get(url, auth=('token', apiKey)) 

repoJSON = response.json() #print (response.json()) 
filename = "repo_info.json"
with open(filename, 'w') as fp: 
    json.dump(repoJSON, fp, indent=4)