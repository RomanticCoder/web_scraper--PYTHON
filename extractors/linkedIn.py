
from requests import get
from bs4 import BeautifulSoup

def extract_linkedIn_jobs(keyword):
  base_url = 'https://www.linkedin.com/jobs/search/?keywords='
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("error")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    jobs = soup.find('ul',class_="jobs-search__results-list")

    job_posts = jobs.find_all('li',recursive=False)
    for job in job_posts:
      anchor = job.find("a", class_="base-card__full-link")
      info = job.find("div", class_="base-search-card__info")

      link = anchor["href"] 
      position = info.find("h3",class_="base-search-card__title")
      companyWrapper = info.find("h4",class_="base-search-card__subtitle")
      company =(companyWrapper.find('a', class_="hidden-nested-link"))
      region = info.find("span",class_="job-search-card__location")
      job_data = {
        'link':link,
        'company':company.string.strip().replace(',',"-"),
        'region':region.string.strip().replace(","," "),
        'position':position.string.strip().replace(","," "),
      }
      results.append(job_data)
    return results

# extract_linkedIn_jobs('python')