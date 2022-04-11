from bs4 import BeautifulSoup
import requests
def find_jobs():
    URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            print(f"Company Name: {company_name.strip()}")
            print(f"skills: {skills.strip()}")
            print(f"description link: {more_info.strip()}")
            description_html = requests.get(more_info).text
            description_soup = BeautifulSoup(description_html,'lxml')
            description = description_soup.find('div', class_='jd-desc job-description-main')
            print(description.text)

if __name__ == '__main__':
    find_jobs()