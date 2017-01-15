# Pull all wiki country pics

from bs4 import BeautifulSoup
import requests
import re
import urllib
import urllib2
import os
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_country_data(filename):
    return json.load(open(filename))

country_data = get_country_data('country_data.json')
countries = country_data.keys()
alpha3 = country_data.values()

country_links = []
for country in (countries + alpha3):
    # Build query string for searching
    query = country.lower() + ' orthographic svg wiki site:commons.wikimedia.org'
    query = '+'.join(query.split())

    # Build HTTP request
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    # Send HTTP GET request, receive soup
    soup = get_soup(url, header)

    try:
        # Grab the first image
        img = soup.find("div", {"class":"rg_meta"})

        # Save the link from the json information
        link = json.loads(img.text)["ou"]

        country_links.append((country, link))
        print (country, link)

        # Save the image locally
        urllib.urlretrieve(link, os.path.join("country_pics", country.replace(' ','_') + '.png'))
    except:
        pass



