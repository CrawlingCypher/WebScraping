#Importssdfds
from bs4 import BeautifulSoup
import requests

url = 'https://www.myprotein.com/elysium.search?search=protein+powder'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", 
          "X-Amzn-Trace-Id": "Root=1-63fcc589-1d94bd4a733cb2a37da42203"}

page = requests.get(url, headers=header)

data = BeautifulSoup(page.content, 'html.parser')


lists = data.find_all('div', class_='athenaProductBlock')

def findPrice(span):
    if span != None:
        return str(span)[43:48]
    return None    

def find_image_source(img):
    img = str(img)
    indexOfSrc = img.find('src="h')
    indexOfEndSrc = img.find('jpg')
    return img[indexOfSrc:indexOfEndSrc+4]
        

for list in lists:
    title = list.find('h3', class_='athenaProductBlock_productName').text.replace('\n','').strip()
    rating = list.find('span', class_='athenaProductBlock_ratingValue').text.replace('\n','').strip()
    customer_reviews = list.find('span', class_='athenaProductBlock_reviewCount').text.replace('\n','').strip()
    price = list.find('span', {'class': 'athenaProductBlock_fromValue'})
    img = list.find('img', class_='athenaProductBlock_image')

   
    info = [title, rating, customer_reviews, findPrice(price), find_image_source(img)]
    print(info)