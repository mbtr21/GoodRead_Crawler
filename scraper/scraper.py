import requests
import pandas as pd
from bs4 import BeautifulSoup


# Define a class for scraping data from Goodreads using BeautifulSoup.
class BeautifulSoapScrapper:
    # Initialize the scrapper with a search query and a type ('books' or 'groups').
    def __init__(self, query, type):
        self.query = query
        self.type = type
        self.category_links = {'books': list(), 'groups': list()}

    # Formulate and store the search URL based on the query and type.
    def request(self):
        try:
            # Replace spaces in the query with '+' for URL compatibility.
            self.query = self.query.replace(' ', '+')
            # Construct the search URL using the formatted query and type.
            base_url = ('https://www.goodreads.com/search?q={query}&search%5Bsource%5D'
                        '=goodreads&search_type={type}&tab={type}')
            # Format the base URL with the query and type, then store it.
            page_urls = base_url.format(query=self.query, type=self.type)
            self.category_links[self.type].append(page_urls)
        except Exception as error:
            # Catch and print any errors encountered during URL formation.
            print(f"Error during URL formation: {error}")

    # Parse the HTML of the book search result page to extract book links.
    def html_book_parsing(self):
        books_link = []
        try:
            # Iterate through each stored URL in the category_links dictionary.
            for link in self.category_links[self.type]:
                response = requests.get(link)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Find all book title links on the page.
                    book_links = soup.find_all('a', attrs={'class': 'bookTitle'})
                    # Extract and format each book link, then add it to the list.
                    book_links = ['https://www.goodreads.com' + link.get('href') for link in book_links if link]
                    books_link.extend(book_links)
                else:
                    # Report a failed request for the current URL.
                    print(f"Failed to fetch data from {link}")
        except Exception as error:
            # Catch and report any errors encountered during HTML parsing.
            print(f"Error during HTML parsing for books: {error}")
        return books_link

    # Extract and compile data for each book from its detailed page.
    def get_data_book_parsing(self):
        # Define the data fields to be extracted from each book page.
        data_fields = [
            ('book_title', 'h1', {'class': 'Text Text__title1'}),
            ('author', 'span', {'class': 'ContributorLink__name'}),
            ('rating', 'div', {'class': 'RatingStatistics__rating'}),
            ('number_of_ratings', 'span', {'data-testid': 'ratingsCount'}, True),
            ('number_of_reviews', 'span', {'data-testid': 'reviewsCount'}, True),
            ('summary', 'span', {'class': 'Formatted'}),
            ('genres', 'span', {'class': 'BookPageMetadataSection__genreButton'}, False, True),
            ('pages_format', 'p', {'data-testid': 'pagesFormat'}),
            ('publication_info', 'p', {'data-testid': 'publicationInfo'})
        ]
        # Initialize a dictionary to store the extracted data.
        data = {field[0]: [] for field in data_fields}
        # Retrieve the list of book links previously parsed.
        books_link = self.html_book_parsing()

        # For each book link, request the page and extract the specified fields.
        for link in books_link:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    # Extract each data field from the page and add it to the data dictionary.
                    for field in data_fields:
                        key, tag, attrs = field[:3]
                        is_numeric = field[3] if len(field) > 3 else False
                        is_list = field[4] if len(field) > 4 else False
                        # Handle fields that are lists or require numeric processing.
                        if is_list:
                            items = soup.find_all(tag, attrs)
                            data[key].append([item.text for item in items] if items else None)
                        else:
                            item = soup.find(tag, attrs)
                            text = item.text if item else None
                            if is_numeric:
                                text = ''.join(filter(str.isdigit, text)) if text else None
                            data[key].append(text)
                else:
                    # Report a failed request for the current book link.
                    print(f"Failed to fetch data from {link}")
            except Exception as error:
                # Catch and report any errors encountered during data extraction.
                print(f"Error during data parsing for books: {error}")

        # Convert the data dictionary into a pandas DataFrame and return it.
        return pd.DataFrame(data)


