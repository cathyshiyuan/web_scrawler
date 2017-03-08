#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:49:55 2017

@author: Cathy
"""

from urllib import urlretrieve, urlopen
from bs4 import BeautifulSoup as bs
import os

download_directory = '/Users/Cathy 1/Desktop/python/'
base_url = 'http://starbucks.com.sg/'

#==============================================================================
# html = urlopen(url)
# soup = bs(html,'lxml')
# img_location = soup.find('a', id = 'logo').find('img')['src']
# 
# print 'Image is downloading......'
# urlretrieve(img_location, 'logo.jpg')
# print 'Download finished!'
#==============================================================================

def get_absolute_url(base_url, source):
    if source.startswith('http://www.'):
        url = 'http://' + source[11:]
    elif source.startswith('http://'):
        url = source
    elif source.startswith('www.'):
        url = 'http://' + source[4:]
    else:
        url = base_url + '/' + source
    if base_url not in url:
        return None
    return url


def get_download_path(base_url, absolute_url, download_directory):
    path = absolute_url.split('/')[-1]
    #path = path.replace(base_url,'')
    path = download_directory + path
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen('http://www.starbucks.com.sg/')
soup = bs(html, 'lxml')
download_list = soup.findAll('img')  # find all img path with src attribute
#print download_list[1]['src']

for download in download_list:
    file_url = get_absolute_url(base_url, download['src'])
    #print file_url
    if file_url is not None:
        print "Downloading from: " + file_url
        try:
            urlretrieve(file_url, get_download_path(base_url, file_url, download_directory))
            print 'Download finished!'
        except:
            print 'Ooops, download failed, next..'
        

print 'Program finished!'




