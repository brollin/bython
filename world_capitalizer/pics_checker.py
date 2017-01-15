# pics_checker.py
# The idea is that with country_pic_puller.py, you have a directory that is
# full of .png pictures.  Some are the full country name style, such as:
# "Bangladesh.png".  Others are the ISO Alpha-3 standard style, such as:
# "ANT.png".  BEFORE this script is run, one must run country_pic_puller.py
# and then manually peruse these pictures, deleting the ones that are not
# the orthographic ones we wish to use in the app.  This must be done 
# manually, unfortunately.  Then, after the desired pictures have been removed,
# this script will note and report back which 'style' country picture was
# chosen.  This can be used by the Android app to find the right image.

import os
import json
import pprint
import shutil

def get_country_data(filename):
    return json.load(open(filename))

country_data = get_country_data('country_data.json')
countries = country_data.keys()
alpha3 = country_data.values()

path = "country_pics"

files = os.listdir(path)
files = [f.replace('.png','').replace('_',' ') for f in files]

country_img_type = {}
for country in countries:
    country_img_type[country] = {}
    country_img_type[country]['full'] = False
    country_img_type[country]['alph'] = False

    if country in files:
        # file has full country in filename
        country_img_type[country]['full'] = True
    if country_data[country] in files:
        # file has alpha3 in filename
        country_img_type[country]['alph'] = True
    
    full = country_img_type[country]['full']
    alph = country_img_type[country]['alph']

    if full and alph:
        pass
        print 'full and alph for', country
    elif full and not alph:
        pass
        print 'full for         ', country
    elif alph and not full:
        pass
        print 'alph for         ', country
    elif not alph and not full:
        print 'no full or alph  ', country

    dest_path = './country_pics_final/' + country.replace(' ','_') + '.png'

    if full:
        shutil.copy('./country_pics/'+country.replace(' ','_')+'.png', dest_path)
    elif alph:
        shutil.copy('./country_pics/'+country_data[country].replace(' ','_')+'.png', dest_path)
    
        

