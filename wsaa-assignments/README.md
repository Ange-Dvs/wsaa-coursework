# WSAA-ASSIGNMENTS
This repository contains the assignments for Semester 3 Web Services and Applications. 

## Cloning the repository from GitHub

WSAA is based in a parent directory for the WSAA module for the semester containing two subfolders, one for the course assignment and the other for labs. 

## Cloning parent repository from GitHub

1. Copy the following URL:
https://github.com/Ange-Dvs/wsaa-coursework.git

2. Open CMDER or if using VS Code open the terminal pane

3. Navigate to the folder where you want to clone the repository to on your machine and type git pull
``git clone https://github.com/Ange-Dvs/wsaa-coursework.git``

4. Set merge as the mode for the pull
``git config pull.rebase false``

5. Initiate the pull of the GitHub repository
``git pull``

6. If the pull has been successful, you should see 6 files pulled from GitHub. The ``readme.md`` for the parent directory, the ``.gitignore`` file, the 2 subfolders mentioned above ``wsaa-assignments`` and ``wsaa-labs``
Only the subfolder ``wsaa-assignments`` is relevant for the assignments for the semester.  
Within, the ``wsaa-assignments`` 5 files will be within, this ``README.md``, 3 assignment files and ``cso.json`` which is the output of ``assignment03-cso.py``.

## Software used
The software used for the creation of the assignment notebooks included VS Code, Python, Jupyter notebooks & GitHub. 

## Walkthrough of assignments
This next section will walkthrough each assignment at a high level to discuss the steps taken within each. 

### wsaa-assignments/assignment2-carddraw.ipynb
This program interacts with an API which simulates dealing a deck of cards.
It then shuffles the deck, get's the ``deck_id``, get's the cards and prints the value and suit of each card.

#### Key Steps

1. **Shuffle a new deck**:
   - A `GET` request is sent to `https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1`
   - The response contains a `deck_id` to uniquely identify the shuffled deck.
   ```python
   deck_count = rq.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
   ```

2. **Draw cards**:
   - Another `GET` request is sent using the `deck_id` to draw 5 cards.
   - The response includes details of each drawn card (value and suit).
   ```python 
   cards = rq.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={no_of_cards}')
   cards_response = cards.json()
   cards_drawn = cards_response['cards']
   ```

3. **Print the drawn cards**:
   - The cards are printed in order the order they are drawn using enumerate to loop through the ``cards_drawn`` list, showing the value and suit for each card.
    ```python 
    for i, card in enumerate(cards_drawn, start=1):
        print(f'Card {i} = {card["value"]} of {card['suit']}')
    ```

### wsaa-assignments\assignment03-cso.py
This program retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called ``cso.json``.

#### Locating the data 
Within the data.cso.ie website, on the left hand pane select Economy > Finance > Finance Indicators. 
This will being you to the results for the Finance Indictors. 

In the results you will find the page for FIQ02 - Exchequer Account (Historical Series) dataset, [direct link here](https://data.cso.ie/table/FIQ02).

In this page in the API Data Query section the RESTful API link can be found, [direct link here](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en).

#### Key steps
- **URL Construction**:  
The program forms the dataset URL within the ``getAll()`` function using a base string and appends the dataset code and formatting type.
    ```python
    url = urlBegining + dataset + urlEnd
    ```

- **GET Request**:  
A ``GET`` request is made to the CSO API to retrieve the dataset in JSON-stat format.
    ```python
    def getAll(dataset):
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json
    ```

- **Saving the Data**:  
The response is converted to a JSON string and written to a file called ``cso.json``.
    ```python
    def getAllAsFile(dataset):
        with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)
    ```

- **Functionality Overview**:  
``getAll(dataset)``: Pulls and returns the ``JSON`` response from the CSO API.  
``getAllAsFile(dataset)``: Saves the data returned by ``getAll()`` into ``cso.json``.

### wsaa-assignments/assignment04-github.py
This program reads a text file from a private repository and replaces all the instances of occurrences of "Andrew" with "Angela". 
It then commits those changes and pushes the file back to the repository.

#### Key Functional Steps

- **API Authentication**:  
  The script authenticates using a GitHub personal access token stored securely in a separate ``config.py`` file:
    ```python
    from config import config as cfg
    apiKey = cfg['githubkey']
    ```

- **File Retrieval**:  
  A ``GET`` request is made to the GitHub API to fetch the contents of ``sample_file_for_assignment04.txt``.
  
  ```python 
  response = requests.get(file_url, headers=headers)
  ```

- **Data Processing**:
  - The file content is base64-decoded.
  - Every instance of the name ``"Andrew"`` is replaced with ``"Angela"``.
  - The new content is base64-encoded.
    ```python 
    file_content = base64.b64decode(file_data['content']).decode()
    updated_content = file_content.replace('Andrew', my_name)
    encoded_content = base64.b64encode(updated_content.encode()).decode()
    ```

- **File Update**:  
  A ``PUT`` request is made to commit the updated content to the same file on the ``main`` branch.
    ```python 
    update_response = requests.put(file_url, headers=headers, data=json.dumps(update_data))
    ```

- **Response Handling**:
  - ``.json()`` is used to parse the response into a Python dictionary to access message details.
  - The ``GET`` request response is first checked for ``200`` status code, throwing an error informing the user there was an error fetching the file if ``200`` is not returned.
  - Within this ``if`` statement, after the update is performed success is confirmed with status codes ``200`` or ``201``; otherwise, the error message is printed.
    ```python 
    if response.status_code == 200:
        ... #main body of code removed to show the error handling
        if update_response.status_code in [200, 201]:
            print(f'Successfully updated {file_path} and pushed changes to GitHub')
        else:
            print(f'Error updating file: {update_response.status_code} - {update_response.json()}')
    else:
        print(f'Error fetching file: {response.status_code} - {response.json()}')
    ```

#### Note
- The program accesses a **private repository**, with this the GitHub token used must have appropriate repo access.
- If trying to use the program for another repo the ``my_name``, ``repo_owner``, ``repo_name``, and ``file_path`` files would need to be updated to the appropriate values.

## Libraries Used

Within the assignments, various libraries are used including:
- ``requests``
- ``base64``
- ``config`` (custom/local module)
- Built-in/Standard library

<font size="4"><b>requests</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The ``requests``[^1] library is used to send HTTP requests in a simple and user-friendly way. It is central to the interaction with external APIs such as the CSO API and the GitHub API.

The following methods from ``requests`` are used across the assignments:

> ``.get`` (Function) – Sends a GET request to retrieve data from a specified URL. [^2]  

> ``.put`` (Function) – Sends a PUT request to update a file in a GitHub repository (used with JSON payload and headers).[^3]  

> ``.json()`` (Method) – Decodes the ``JSON`` response body (if any) as a ``Python`` object. Depending on the response the output may vary, possibilities include ``dicts`` and ``lists``.[^4]  

<font size="4"><b>base64</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The ``base64`` library provides functions to encode and decode data in Base64 — used in ``assignment04-github.py`` when working with GitHub’s API, which require file content to be base64-encoded for updates. [^5]

> ``.b64decode`` (Function) – Decodes a base64-encoded string back into plain text [^6].  

> ``.b64encode`` (Function) – Encodes plain text data into base64 format [^7].  

<font size="4"><b>config</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A custom module named ``config`` is used in ``assignment04-github.py`` to securely store the GitHub API key needed to authenticate with the private repository.

> ``config as cfg`` – Imports the config dictionary containing authentication credentials (e.g., ``cfg['githubkey']``).  

<font size="4"><b>Default Python Functionality (Built-in or Standard Library)</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Built-in Python methods are used for data handling, logic, and file writing.

> ``enumerate`` (Function) – Works as a way to loop over objects while also keeping count for the loop. The function takes in two arguments, the sequence to be used for the loop and optionally the starting value for the loop. In ``assignment2-carddraw.ipynb`` it is used to index drawn cards for so the user can clearly see which order the cards were drawn in when displaying the results.[^8]  

> ``open`` (Function) – Opens a file (e.g., ``cso.json``) and returns it as a file object used for writing the output of the file.[^9]  

> ``with`` (Keyword) – Used with ``open`` and write to a file.[^10]  

> ``if __name__ == "__main__"`` – Ensures the script only runs when executed directly.[^11]  

> ``.dumps()`` (Function from ``json`` module [^12]) – Converts a Python object into a JSON-formatted string (used for writing to a file or sending data in API calls)[^13].

***
End

**Author:**
Angela Davis

[^1]: https://docs.python-requests.org/en/latest/
[^2]: https://docs.python-requests.org/en/latest/api/#requests.get
[^3]: https://docs.python-requests.org/en/latest/api/#requests.put
[^4]: https://requests.readthedocs.io/en/latest/api/#requests.Response.json
[^5]: https://docs.python.org/3/library/base64.html
[^6]: https://docs.python.org/3/library/base64.html#base64.b64encode
[^7]: https://docs.python.org/3/library/base64.html#base64.b64decode
[^8]: https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python#what_does_enumerate_do_in_python
[^9]: https://www.w3schools.com/Python/ref_func_open.asp
[^10]: https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/#:~:text=How%20Does%20the%20With%20Statement%20Work%20in%20Python%3F 
[^11]: https://www.datacamp.com/tutorial/if-name-equals-main-python  
[^12]: https://docs.python.org/3/library/json.html
[^13]: https://docs.python.org/3/library/json.html#json.dumps