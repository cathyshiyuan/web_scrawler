#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 16:02:16 2017

@author: Cathy
"""

from urllib import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup as bs
import re
import random
import datetime

#random.seed(datetime.datetime.now())
url = 'https://en.wikipedia.org'
pages = set()

def getLinks(articleUrl):
    html = urlopen(url + articleUrl)    
    bsObj = bs(html.read(),'lxml')
    #compiled_link = re.compile('^(/wiki/)((?!:).)*$')    article
    compiled_link = re.compile('^(/wiki/)')    # insite link
    try:
        print bsObj.h1.get_text()
        print bsObj.find(id = 'mw-content-text').findAll('p')[0]
        print bsObj.find(id = 'ca-edit').find('span').find('a').attrs['href']
    except AttributeError:
        print 'This page is missing someting!'
    
    for link in bsObj.findAll('a', href = compiled_link):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                print '------------------------\n' + new_page
                pages.add(new_page)
                getLinks(new_page)

getLinks('')
        

#==============================================================================
# 
#   random walk from site to site
#links = getLinks('/wiki/Kevin_Bacon')
# 
# while len(links) > 0:
#     new_article = links[random.randint(0,len(links)-1)].attrs['href']
#     print new_article
#     links = getLinks(new_article)
#==============================================================================
    

#==============================================================================
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = bs(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# 
# title = getTitle('http://www.pythonscraping.com/exercises/exercise1.html')
# if title == None:
#     print 'Title could not be found'
# else:
#     print title
#==============================================================================








                                                                                                             