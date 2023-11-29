import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/python/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print("Title:", title)
else:
    print("Failed to retrieve the webpage.")
