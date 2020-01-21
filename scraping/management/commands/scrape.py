import os

import requests
from django.core.management import BaseCommand
from bs4 import BeautifulSoup
from urllib.request import urlopen

from django.db import IntegrityError

from scraping.models import Job


def pages_count():
    link = "https://career.habr.com/vacancies?remote=1&skills%5B%5D=446&type=all"
    html = urlopen(link)

    soap = BeautifulSoup(html, 'html.parser')
    pages = soap.find_all('a', class_='page')

    if pages:
        return int(pages[-1].text)
    else:
        return 1


def scrape():
    base_url = 'https://career.habr.com'

    for page in range(1, pages_count() + 1):
        link = f'https://career.habr.com/vacancies?remote=1&skills%5B%5D=446&page={page}&type=all'
        html = urlopen(link)
        soap = BeautifulSoup(html, 'html.parser')
        jobs = soap.find_all('div', class_='job')
        for job in jobs:
            href = job.find('div', class_='title').find('a')['href']
            title = job.find('div', class_='title').find('a').text
            try:
                location = job.find('span', class_='location').find('a').text
            except AttributeError:
                location = 'No location'
            try:
                salary = job.find('div', class_='salary').find('div').text
            except AttributeError:
                salary = 'No salary'
            company_name = job.find('span', class_='company_name').find('a').text

            try:
                Job.objects.create(link=base_url+href, title=title, location=location, salary=salary, company_name=company_name)
                print(f'{title} added')
                send_text = 'https://api.telegram.org/bot' + os.environ["TOKEN"] + '/sendMessage?chat_id=' + '128181451' + '&parse_mode=Markdown&text=' + base_url+href
                requests.get(send_text)
            except IntegrityError:
                print(f'{title} already exists')


class Command(BaseCommand):
    help = "testing"

    def handle(self, *args, **options):
        scrape()
