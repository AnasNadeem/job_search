# https://in.linkedin.com/jobs/search?keywords=Website%20development
# &location=India&geoId=102713980&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0

import requests
from bs4 import BeautifulSoup

param_query = {'keywords':'website',
                'location':'India',
                # 'geoId':102713980,
                'trk':'public_jobs_jobs-search-bar_search-submit',
                'pageNum':0
                }
r = requests.get('https://in.linkedin.com/jobs/search', params=param_query).text
soup = BeautifulSoup(r, 'lxml')

for i in soup.find_all('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card'):
    # Getting link of job 
    # all_job_link.append(f"https://in.indeed.com/{i.attrs['href']}")
    job_link = i.find('a', class_="base-card__full-link").attrs['href']
    # Getting all the other data
    job_card = i.find('div', class_='base-search-card__info')
    # Job Title 
    job_title = job_card.find('h3', class_='base-search-card__title').text
    # Company Title
    job_comp_title = job_card.find('h4', class_='base-search-card__subtitle').text
    # Location Title
    job_comp_location = job_card.find('span', class_='job-search-card__location').text

    print(job_title.strip(), job_comp_title.strip(), job_comp_location.strip())