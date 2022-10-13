from reprlib import recursive_repr
from requests import get
from bs4 import BeautifulSoup

from extractors.wwr import extract_wwr_jobs
from extractors.linkedIn import extract_linkedIn_jobs
print("\nWhat kind of job are you looking for? \n")
keyword = input("type the keyword: ")

file = open(f"{keyword}_jobs.csv", "w")

file.write("Position, Company, Location, URL\n")

linkedIn = extract_linkedIn_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = linkedIn + wwr

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['region']},{job['link']}\n" )