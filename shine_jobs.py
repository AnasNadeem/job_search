import requests
from bs4 import BeautifulSoup
# position_title = 'website'
# r = requests.get(f'https://www.shine.com/job-search/{position_title}-jobs').text
# soup = BeautifulSoup(r, 'lxml')
# print(soup.title)

try:
    indeed_param_query = {'q':'website','l':''}
    indeed_request = requests.get('https://in.indeed.com/jobs', params=indeed_param_query).text
    indeed_soup = BeautifulSoup(indeed_request, 'lxml')
    indeed_jobs_list = []
    for i in indeed_soup.find_all('a', class_='tapItem'):
        # Getting link of job 
        indeed_job_link = f"https://in.indeed.com{i.attrs['href']}"
        # Getting all the other data
        indeed_job_card = i.find('div', class_='job_seen_beacon')
        # Job Title 
        indeed_job_pos = indeed_job_card.find('h2', class_='jobTitle')
        indeed_job_pos_text = indeed_job_pos.find('span', title=True).text
        # Company Title
        indeed_job_comp_title = indeed_job_card.find('span', class_='companyName').text
        # Location Title
        indeed_job_comp_location = indeed_job_card.find('div', class_='companyLocation').text

        indeed_job_skills_list = []
        indeed_job_skills = indeed_job_card.find('div', class_="job-snippet")
        for skill in indeed_job_skills.find_all('li'):
            indeed_job_skills_list.append(skill.text)
        print(indeed_job_skills_list)

        # Salary Title
        try:
            indeed_job_salary = indeed_job_card.find('span', class_='salary-snippet').text
        except:
            indeed_job_salary= ''
        indeed_job_list = [indeed_job_comp_title, indeed_job_pos_text, indeed_job_comp_location, indeed_job_salary, indeed_job_link, 'Indeed']
        indeed_jobs_list.append(indeed_job_list)
    # all_jobs_list.append(indeed_jobs_list)

except Exception as e:
    print(f'Error occured {e}')
# # Get all the joblist
# all_job_link = []
# for i in soup.find_all('a', class_='tapItem'):
#     # Getting link of job 
#     # all_job_link.append(f"https://in.indeed.com/{i.attrs['href']}")

#     # Getting all the other data
#     job_card = i.find('div', class_='job_seen_beacon')

#     # Job Title 
#     job_title = job_card.find('h2', class_='jobTitle')
#     job_title_text = job_title.find('span', title=True).text
#     # Company Title
#     job_comp_title = job_card.find('span', class_='companyName').text
#     # Location Title
#     job_comp_location = job_card.find('div', class_='companyLocation').text
#     # Salary Title
#     try:
#         job_salary = job_card.find('span', class_='salary-snippet').text
#     except:
#         job_salary= ''
    
