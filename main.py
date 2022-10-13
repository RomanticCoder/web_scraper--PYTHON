from extractors.wwr import extract_wwr_jobs
from extractors.linkedIn import extract_linkedIn_jobs
from file import save_to_file

print("\nWhat kind of job are you looking for? \n")
keyword = input("type the keyword: ")

linkedIn = extract_linkedIn_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = linkedIn + wwr

save_to_file(keyword, jobs)