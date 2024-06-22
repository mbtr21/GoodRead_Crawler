from celery import shared_task
from .scraper import BeautifulSoapScrapper
from .models import Book, Group


@shared_task()
def process_data_task(search, selection):
    print(f"Selection: {selection}, Search: {search}")
    soup = BeautifulSoapScrapper(query=search, type=selection)
    soup.request()
    if selection == 'books':
        data = soup.get_data_book_parsing()
        for index, row in data.iterrows():
            instance = Book(
                title=row['book_title'],
                description=row['summary'],
                author=row['author'],
                rate=row['rating'],
                numbers_of_ratings=row['number_of_ratings'],
                numbers_of_reviews=row['number_of_reviews'],
                genres=row['genres'],
                pages_format=row['pages_format'],
                publication_info=row['publication_info']
            )
            instance.save()
    else:
        data = soup.get_group_data_parsing()
        for index, row in data.iterrows():
            instance = Group(
                title=row['group_title'],
                description=row['description'],
                tags=row['tags'],
                rules=row['rules'],
                categories=row['category'],
                website=row['website'],
                location=row['location'],
                group_type=row['group type']

            )
            instance.save()
    return {"processed_data": f"Processed {selection} and {search}"}