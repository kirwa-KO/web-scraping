import requests
from bs4 import BeautifulSoup
from random import random

# get the link of the product
URL = input("Please Entre the Product link: ")
# URL = "https://www.etsy.com/listing/889413725/satin-pouch?ref=hp_rv-2"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# get the product images
allImages = soup.findAll('img', attrs={'class' : "wt-max-width-full wt-horizontal-center wt-vertical-center carousel-image wt-rounded"})
imageCounter = 0
for i in allImages:
	for j in str(i).split():
		if "src=" in j:
			imgSrc = j.split('"')[1]
			response = requests.get(imgSrc)
			if imageCounter == 0:
				imageName = "mainImage.jpg"
			else:
				imageName = "image" + str(imageCounter) + ".jpg"
			imageCounter += 1
			file = open(imageName, "wb")
			file.write(response.content)
			file.close()

# get product title
productTitle = str(soup.find('h1', attrs={'class' : 'wt-text-body-03'}))
productTitle = ((productTitle.split('>')[1]).split("<")[0]).strip()
print("Title: " + productTitle)

# get product description
productDesc = str(soup.find('p', attrs={'class' : 'wt-text-body-01 wt-break-word'}))
productDesc = ((productDesc.replace("<br/>", "\n").split('>')[1]).split("<")[0]).strip()
print('Description:')
print(productDesc)
