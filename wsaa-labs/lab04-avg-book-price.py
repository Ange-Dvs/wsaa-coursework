import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"

def get_all_books():
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching books: {e}")
        return None

def calculate_average_price():
    books = get_all_books()
    if not books:
        print("No books found or failed to fetch books.")
        return None

    prices = []  # Initialize an empty list for prices

    # Loop through books and extract valid prices
    for book in books:
        if "price" in book and isinstance(book["price"], (int, float)):
            prices.append(book["price"])

    if not prices:  # Check if prices list is empty
        print("No valid book prices found.")
        return None

    average_price = sum(prices) / len(prices)  # Calculate average
    return round(average_price, 2)  # Round for readability


if __name__ == "__main__":
    avg_price = calculate_average_price()
    if avg_price is not None:
        print(f"Average book price: €{avg_price}")
