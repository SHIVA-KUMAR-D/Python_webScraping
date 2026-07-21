import requests
from bs4 import BeautifulSoup

url=input("enter the url:")
response=requests.get(url,timeout=5)
soup=BeautifulSoup(response.text,"html.parser")
print(f"{type(soup)}, {type(response.text)}")
print(f"{type(soup.head)}")
print(f"{type(soup.body)}")
print(f"{type(soup.title)}")
print(f"{soup.title.text}")
print("="*50)
