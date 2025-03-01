# lab04-requests.py
# Python file for the lab associated with week 4.
# Author: Angela Davis

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks(): 
    try:
        response = requests.get(url)
        response.raise_for_status()  # raising an error for HTTP failures    
        return response.json() # retruning the API response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching books: {e}") # printing an error is thrown
        return None

def readbook(book_id):   
    geturl = url + "/" + str(book_id)     
    try:  
        response = requests.get(geturl)     
        response.raise_for_status()  # raising an error for HTTP failures    
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching book with ID {book_id}: {e}")
        return None
    
def createbook(book):
    try:
        response = requests.post(url, json=book)
        response.raise_for_status()  # raising an error for HTTP failures    
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"Error creating book: {e}")
        return None
    
def updatebook(book_id, book):
    puturl = url + "/" + str(book_id)   
    try:
        response = requests.put(puturl, json=book)
        response.raise_for_status()  # Raise error for failed requests (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error updating book with ID {book_id}: {e}")
        return None
    
def deletebook(book_id):     
    deleteurl = url + "/" + str(book_id)     
    try:
        response = requests.delete(deleteurl)
        response.raise_for_status() 
        # Some APIs return a 204 No Content on DELETE, so we check the response
        if response.status_code == 204:
            return {"message": f"Book ID {book_id} successfully deleted."}
        return response.json()  # if there's a response body, return it

    except requests.exceptions.RequestException as e:
        print(f"Error deleting book with ID {book_id}: {e}")
        return None

def test_readbook():
    test_id = 550  
    
    print(f"Testing book retrieval with ID {test_id}...")
    book = readbook(test_id)
    
    if book:
        print("Book retrieved successfully:", book)
    else:
        print("Book retrieval failed.")

def test_createbook():
    test_book = {
        "title": "Test Book",
        "author": "John Doe",
        'id': 9999,
        "price": 12.99
    }
    
    print("Testing book creation...")
    created_book = createbook(test_book)
    
    if created_book:
        print("Book created successfully:", created_book)
    else:
        print("Book creation failed.")

def test_updatebook():
    test_id = 550 
    updated_book = {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "price": 44
    }
    
    print(f"Testing book update for ID {test_id}...")
    updated_response = updatebook(test_id, updated_book)
    
    if updated_response:
        print("Book updated successfully:", updated_response)
    else:
        print("Book update failed.")

def test_deletebook():
    test_id = 1612  # id returned when creating the book
    
    print(f"Testing book deletion for ID {test_id}...")
    delete_response = deletebook(test_id)
    
    if delete_response:
        print("Book deleted successfully:", delete_response)
    else:
        print("Book deletion failed.")

if __name__ == "__main__": 
    print (readbooks()) 
    print (readbook(1612))
    # test_createbook() # 1614, 1613 ids created
    # test_updatebook() # 1614, 1613, 1612 testing the updating of the book
    # test_deletebook() # 1614, 1613, 1612 testing the deletion of the book