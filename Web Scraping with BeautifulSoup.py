import requests
from bs4 import BeautifulSoup

url = "https://moodle.jessup.edu/login/index.php"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print("Title:", title)
else:
    print("Failed to retrieve the webpage.")
