import urllib.request 
from bs4 import BeautifulSoup
  
url = "https://punchng.com/breaking-polls-rivers-rep-member-arrested-with-foreign-currency/"

html = urllib.request.urlopen(url)
  
htmlParse = BeautifulSoup(html, 'html.parser')
for para in htmlParse.find_all("p" ,limit=20):
    print(para.get_text())