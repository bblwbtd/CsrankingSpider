import csv

from bs4 import BeautifulSoup


def extract_page_text(page: str) -> str:
    soup = BeautifulSoup(page, 'html.parser')

    return '\n'.join(list(filter(lambda x: x != '', soup.text.splitlines())))


def extract_professor_information(csv_text: str):
    reader = csv.reader(csv_text.splitlines()[2:])
    return list(reader)
