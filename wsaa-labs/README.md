# wsaa-labs
README.md for adding some additional references used throughout the labs.

### Lab05 
- GitHub API – Create or Update File: https://docs.github.com/en/rest/repos/contents#create-or-update-file-contents
- Article on importing and exporting files to GitHub via API (using PyGithub): https://medium.com/plumbersofdatascience/import-and-export-files-to-and-from-github-via-api-626efd7dd859 
- Base64 encoding returns bytes: https://docs.python.org/3/library/base64.html#base64.b64encode
- JSON uses strings, not bytes: https://docs.python.org/3/library/json.html#json.dump:~:text=fp%20(file%2Dlike%20object)%20%E2%80%93%20The%20file%2Dlike%20object%20obj%20will%20be%20serialized%20to.%20The%20json%20module%20always%20produces%20str%20objects%2C%20not%20bytes%20objects%2C%20therefore%20fp.write()%20must%20support%20str%20input
- .decode() converts bytes to a valid string: https://docs.python.org/3/library/stdtypes.html#str.decode