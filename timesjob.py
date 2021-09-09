import requests
from bs4 import BeautifulSoup
position_title = 'website'
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Website+Development&txtLocation="
param_query = {
    "searchType":"personalizedSearch",
    "from":"submit",
    "txtKeywords":""
}
r = requests.get(f'https://www.shine.com/job-search/{position_title}-jobs').text
soup = BeautifulSoup(r, 'lxml')
print(soup.title)