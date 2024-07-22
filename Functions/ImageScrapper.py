import requests
from bs4 import BeautifulSoup

def image_scrapper(word):
    url = 'https://www.google.com/search?q={0}&tbm=isch'.format(word)
    print("Generating image")
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml') 
    images = soup.findAll('img')
    first_image = images[1]
    return first_image.get('src')