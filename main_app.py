from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html', title='Home')

@app.route('/search-job/', methods=['GET', 'POST'])
def search_job():
    if request.method=='POST':
        job_position = request.form.get('job_position')
        job_location = request.form.get('job_location')
        # List Structure: [comp_title, job_pos, job_loc, job_salary, job_link, job_website, job_skills]
        all_jobs_list = []
        all_jobs_list.append(indeed_jobs(job_position, job_location))
        all_jobs_list.append(linkedin_jobs(job_position, job_location))
        all_jobs_list.append(shine_jobs(job_position, job_location))
        # all_jobs_list.append(times_jobs(job_position, job_location))
        return render_template('resultscard.html',results_list = all_jobs_list)

def indeed_jobs(job_position, job_loc):
    indeed_jobs_list = []
    try:
        # Indeed Queries 
        indeed_param_query = {'q':f'{job_position}','l':f'{job_loc}'}
        indeed_request = requests.get('https://in.indeed.com/jobs', params=indeed_param_query).text
        indeed_soup = BeautifulSoup(indeed_request, 'lxml')
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
            # Salary Title
            try:
                indeed_job_salary = indeed_job_card.find('span', class_='salary-snippet').text
            except:
                indeed_job_salary= ''
            # Job Skills 
            indeed_job_skills = indeed_job_card.find('div', class_="job-snippet")
            indeed_job_skills_list = []
            for skill in indeed_job_skills.find_all('li'):
                indeed_job_skills_list.append(skill.text)
            indeed_job_list = [indeed_job_comp_title, indeed_job_pos_text, indeed_job_comp_location, indeed_job_salary, indeed_job_link, 'Indeed']
            indeed_jobs_list.append(indeed_job_list)
    except Exception as e:
        print(f'Error occured {e}')
    return indeed_jobs_list

def linkedin_jobs(job_position, job_loc):
    linkedin_jobs_list = []
    try:
        # Linkedin Queries 
        linkedin_param_query = {'keywords':f'{job_position}',
                            'location':f'{job_loc}',
                            'trk':'public_jobs_jobs-search-bar_search-submit',
                            'pageNum':0
                            }
        linkedin_request = requests.get('https://in.linkedin.com/jobs/search', params=linkedin_param_query).text
        linkedin_soup = BeautifulSoup(linkedin_request, 'lxml')
        for i in linkedin_soup.find_all('div', class_='base-card base-card--link base-search-card base-search-card--link job-search-card'):
            # Getting link of job 
            linkedin_job_link = i.find('a', class_="base-card__full-link").attrs['href']
            # Getting all the other data
            linkedin_job_card = i.find('div', class_='base-search-card__info')
            # Job Title 
            linkedin_job_position = linkedin_job_card.find('h3', class_='base-search-card__title').text
            # Company Title
            linkedin_job_comp_title = linkedin_job_card.find('h4', class_='base-search-card__subtitle').text
            # Location Title
            linkedin_job_comp_location = linkedin_job_card.find('span', class_='job-search-card__location').text    
            linkedin_job_list = [linkedin_job_comp_title, linkedin_job_position, linkedin_job_comp_location, 'Not Mentioned', linkedin_job_link, 'Linkedin']
            linkedin_jobs_list.append(linkedin_job_list)
    except Exception as e:
        print(f'Error occured {e}')
    return linkedin_jobs_list

def shine_jobs(job_position, job_loc):
    shine_jobs_list = []
    try:
        # https://www.shine.com/job-search/website-developer-jobs-in-mumbai
        job_position_text = job_position.replace(' ', '-')
        if job_loc:
            shine_request = requests.get(f'https://www.shine.com/job-search/{job_position_text}-jobs-in-{job_loc}').text
            shine_soup = BeautifulSoup(shine_request, 'lxml')
            for i in shine_soup.find_all('li', class_='result-display__profile'):
                shine_job_card = i.find('div', class_='w-90 ml-25')
                # Job Title 
                shine_job_title = shine_job_card.ul.li.h2.text
                # Job Link
                shine_job_link = f"https://www.shine.com{shine_job_card.ul.li.h2.a['href']}"
                # Company Title
                shine_job_comp_title = shine_job_card.find('span', class_='result-display__profile__company-name').text
                shine_year_title = shine_job_card.find_all('li', class_="result-display__profile__years")
                shine_location = shine_year_title[1].text
                shine_job_list = [shine_job_comp_title, shine_job_title, shine_location, 'Not Mentioned', shine_job_link, 'Shine']
                shine_jobs_list.append(shine_job_list)
        else:
            shine_request = requests.get(f'https://www.shine.com/job-search/{job_position_text}-jobs').text
            shine_soup = BeautifulSoup(shine_request, 'lxml')
            for i in shine_soup.find_all('li', class_='result-display__profile'):
                shine_job_card = i.find('div', class_='w-90 ml-25')
                # Job Title 
                shine_job_title = shine_job_card.ul.li.h2.text
                # Job Link
                shine_job_link = f"https://www.shine.com{shine_job_card.ul.li.h2.a['href']}"
                # Company Title
                shine_job_comp_title = shine_job_card.find('span', class_='result-display__profile__company-name').text
                shine_year_title = shine_job_card.find_all('li', class_="result-display__profile__years")
                shine_location = shine_year_title[1].text
                shine_job_list = [shine_job_comp_title, shine_job_title, shine_location, 'Not Mentioned', shine_job_link, 'Shine']
                shine_jobs_list.append(shine_job_list)
    except Exception as e:
        print(f'Error occured {e}')
    return shine_jobs_list

# def times_jobs(job_position, job_loc):
#     times_jobs_list = []
#     try:
#         tj_param_query = {
#             "searchType":"personalizedSearch",
#             "from":"submit",
#             "txtKeywords":f"{job_position}",
#             "txtLocation":f"{job_loc}"
#         }
#         tj_request = requests.get(f'https://www.timesjobs.com/candidate/job-search.html', params=tj_param_query).text
#         tj_soup = BeautifulSoup(tj_request, 'lxml')
#         print(tj_soup.title)

#     except Exception as e:
#         print(f'Error occured {e}')
#     return times_jobs_list


if __name__ == '__main__':
    app.run()