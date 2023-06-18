#scraping opendata prescriptions in the community for dictionary 'month year':'sourcefilename'

import requests
from bs4 import BeautifulSoup

def get_dict_of_sources():
    URL='https://www.opendata.nhs.scot/dataset/prescriptions-in-the-community'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    title=[]
    id=[]
    dict_source={}

    for URL in soup.find_all('li'):
        record=str(URL.get('data-id'))
        if record!="None": id.append(record)

    for URL in soup.find_all('a'):
        record=str(URL.get('title'))
        if record.startswith("Prescribing Data"): title.append(record[17:])

    for i in range(len(id), 0, -1): dict_source[title[i-1]]=id[i-1]
    return dict_source

if __name__ == "__main__":
    dict_source=get_dict_of_sources()