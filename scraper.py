import requests
import bs4
import json
import time
import random


jobs = []

# Agent to fake the request as browser to avoid blocking
headers = open("headers.json")
headers = dict(json.load(headers))

def scrape_data(search_query="python"):
    time.sleep(random.randint(1,5))
    #Sends a request
    url = requests.get(f"https://www.upwork.com/search/jobs/?q={search_query}&sort=recency", headers=headers)

    #Parses the html output
    parser = bs4.BeautifulSoup(url.content, 'lxml')
    
    # Gathering all the information
    titles = [i.text.replace("\n", "") for i in parser.find_all('a', class_="job-title-link break visited")]
    
    urls = [ i['href'] for i in parser.find_all('a', class_ ="job-title-link break visited") ]
    descriptions = [ i.text for i in parser.find_all('span', class_ ="js-description-text") ]

    # Making a list of dicts
    for i in range(10):
        job = f"{{ 'title' : '{titles[i]}', 'url' : 'https://upwork.com/{urls[i]}' , 'description' : '''{ descriptions[i] }''' }}"
        jobs.append(eval(job))
    return jobs
   
   
