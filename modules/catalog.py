from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd


class Catalog():
    def __init__(self, catalog):
        self.catalog = catalog
        
    def search(self, input_search):
        list_result = []
        for catalog_item in self.catalog:
            for item in catalog_item:
                if input_search.lower() in item.title.lower():
                    if isinstance(item, Book):
                        list_result.append(f'Title: {item.title}, authors: {item.authors}, Type Catalog: Book')
                    elif isinstance(item, Magazine):
                        list_result.append(f'Title: {item.title}, volume: {item.volume}, Type Catalog: Magazine')
                    elif isinstance(item, Dvd):
                        list_result.append(f'Title: {item.title}, actors: {(item.actors)}, Type Catalog: Dvd')
                    elif isinstance(item, Cd):
                        list_result.append(f'Title: {item.title}, Artist: {item.artist}, Type Catalog: Cd')
        return list_result
