from requests import get
from bs4 import BeautifulSoup

from extractors.wwr import extract_jobs

print(extract_jobs("python"))