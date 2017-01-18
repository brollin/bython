from BeautifulSoup import BeautifulSoup
import requests
import shutil
import os

def download_img(src, name):
    response = requests.get(src, stream=True)
    fileName = name.replace(' ','_')+'.jpg'
    while os.path.isfile(fileName):
        fileName = fileName.replace('.jpg','_.jpg')

    with open(fileName,'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        del response

def wallpaper_scraper(url):
    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html)

    for link in soup.findAll('a'):
        if link.get('href'):
            if link.get('href').startswith('big.php'):
                picReq  = requests.get('https://wall.alphacoders.com/' + link.get('href'))
                picHtml = picReq.text
                picSoup = BeautifulSoup(picHtml)
                
                for img in picSoup.findAll('img'):
                    if img.get('id') == 'main_wallpaper':
                        picSrc  = img.get('src')
                        picName = img.get('title')
                        picName = picName.replace('Earth','').replace('Wallpaper','').strip()
                        picName = picName.split('National')[0].strip()
                        
                        download_img(picSrc, picName)
    
# wallpaper_scraper("https://wall.alphacoders.com/by_collection.php?id=460&page=1")
# wallpaper_scraper("https://wall.alphacoders.com/by_collection.php?id=460&page=2")
wallpaper_scraper("https://wall.alphacoders.com/by_collection.php?id=460&page=3")
wallpaper_scraper("https://wall.alphacoders.com/by_collection.php?id=460&page=4")
wallpaper_scraper("https://wall.alphacoders.com/by_collection.php?id=460&page=5")


