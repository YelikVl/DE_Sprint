# 1. Необходимо спарсить данные о вакансиях python разработчиков с сайта hh.ru, введя в поиск “python разработчик” и указав, что мы рассматриваем все регионы. Необходимо спарсить:

import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
def parse_hh():
    data = {
        "data" : []
    }

    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 '
                       'Firefox/14.0.1'),
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':
        'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding':
        'gzip, deflate',
        'Connection':
        'keep-alive',
        'DNT':
        '1'
    }

    url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post'
    resp = req.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'lxml')
    last_page_tag = soup.find_all(attrs={'data-qa': 'pager-page'})
    last_page = int(last_page_tag[-1].text)
    print(f'last_page: {last_page}')
    for page in tqdm.tqdm(range(0, last_page+1)):
        url = f'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&page={page}&hhtmFrom=vacancy_search_list'
        resp = req.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        tag = soup.find_all(attrs={'class' : 'serp-item__title'})

        for iterator in tag:
            vacancy_name = iterator.text
            url_object = iterator.attrs['href']
            resp_object = req.get(url_object, headers=headers)
            soup_object = BeautifulSoup(resp_object.text, 'lxml')
            salary_tag = soup_object.find(attrs={'data-qa' : 'vacancy-salary'})

            experience_tag = soup_object.find(attrs={'data-qa' : 'vacancy-experience'})
            region_tag = soup_object.find(attrs={'data-qa': 'vacancy-view-location'})

            if not region_tag:
                region_tag = soup_object.find(attrs={'data-qa': 'vacancy-view-raw-address'})
                if region_tag:
                    region_tag_text = region_tag.text.split()[0]
                else:
                    region_tag_text = 'NA'
            else:
                region_tag_text = region_tag.text

            if not salary_tag:
                salary_tag_text = 'NA'
            else:
                salary_tag_text = salary_tag.text

            if not experience_tag:
                experience_tag_text = 'NA'
            else:
                experience_tag_text = experience_tag.text

            data['data'].append({
                'title':vacancy_name,
                'work experience': experience_tag_text,
                'salary': salary_tag_text,
                'region': region_tag_text})

    with open('data.json', 'w') as file:
        json.dump(data, file)