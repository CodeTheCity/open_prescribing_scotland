# get_dict_of_sources: scraping opendata prescriptions in the community for dictionary 'month year':'sourcefilename'
# drugs_from_csv: returns list aggregated unique drugs from input csv with column BNFItemDescription

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

import pandas as pd

def drugs_from_csv (csv):
    df=pd.read_csv(csv)
    print(df)
    lst=df['BNFItemDescription'].values.tolist()
    for i in range(len(lst)):
        if type(lst[i])==float: lst[i]=str(lst[i])
        lst[i]=lst[i][0:lst[i].find(' ')]
        lst[i] = lst[i][0:lst[i].find('_')]
    lst=set(lst)
    lst.remove('')
    return lst


if __name__ == "__main__":
    #dict_source=get_dict_of_sources()
    #print(dict_source)
    csv = "C:/Users\Account\Downloads\pitc202301.csv"
    print(drugs_from_csv(csv))
