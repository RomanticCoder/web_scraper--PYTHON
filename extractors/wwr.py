from requests import get
from bs4 import BeautifulSoup

def extract_jobs(keyword):
  base_url = 'https://weworkremotely.com/remote-jobs/search?term='
  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("not successful")
  else:
    results = []
    # bs4 turn our HTML into Python entity
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.findAll('title'))
    jobs = soup.find_all('section',class_="jobs")
    
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      # remove the last item (<li class="view-all">)
      job_posts.pop()
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        # anchor tag will be stored in dict structure
        link = anchor["href"]
        company, kind, region = anchor.find_all('span', class_="company")
        title = anchor.find('span', class_="title")
  
        job_data = {
          'link':f"https://weworkremotely.com{link}",
          'company':company.string,
          'region':region.string,
          'position':title.string,
          'kind':kind.string
        }
        results.append(job_data)

    return results
  '''
    - positional arguments
    say_hello("Jordan","Good morning")
  
    - keyword arguments
    say_hello(name="Jordan", "Good Evening")
  '''