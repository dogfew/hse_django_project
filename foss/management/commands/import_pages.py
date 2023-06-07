from django.core.management.base import BaseCommand
from foss.models import Page
import os


def import_pages_from_files():
    directory = 'templates/.old/'
    file_extension = '.html'
    pages = [

    ]
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory, filename)
            print(filepath)
            with open(filepath, 'r') as file:
                title = filename[:-len(file_extension)]
                content = file.read()
                pages.append({'title': title,
                              'content': content,
                              'nav': title})
    return pages


class Command(BaseCommand):
    help = 'Import pages into the database'

    def handle(self, *args, **options):
        pages = import_pages_from_files()
        for page_data in pages:
            Page.objects.create(**page_data)