#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:18:26 2017

@author: Cathy
"""
from urllib import urlopen
from bs4 import BeautifulSoup as bs
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

# retrieves a list of all internal links found on a page
def get_internal_links(soup, include_url):
    internal_links = []
    # find all links that begin with a '/'
    compiled_url = re.compile("^(/|.*"+include_url+")")
    for link in soup.findAll('a', href = compiled_url):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internal_links:
                internal_links.append(link.attrs['href'])
    return internal_links

# retrieve a list of all external links found on a page

def get_external_links(soup, exclude_url):
    external_links = []
    #find all links that begins with www or http
    # not contain the current url
    compiled_url = re.compile("^(www|http)((?!"+exclude_url+").)*$")
    for link in soup.findAll('a', href = compiled_url):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in external_links:
                external_links.append(link.attrs['href'])
    return external_links



# split url into a list of components
def split_address(address):
    address_parts = address.replace('http://','').split('/')
    return address_parts   


def get_random_external_link(start_page):
    html = urlopen(start_page)
    soup = bs(html.read(),'lxml')
    external_links = get_external_links(soup, split_address(start_page)[0]) # home page shows server name
    if len(external_links) == 0:
        internal_links = get_internal_links(soup, start_page)
        return get_random_external_link(internal_links[random.randint(0,len(internal_links)-1)])
        # if this page doesn't have external page, choose another internal page and try again
    else:
        return external_links[random.randint(0, len(external_links)-1)]


def follow_external_only(site):
    external_link = get_random_external_link('http://oreilly.com')
    print 'Random external link is: ' + external_link
    follow_external_only(external_link)

#follow_external_only('http://oreilly.com')


# collects a list of all external urls on this site, should add try and exception
all_external_links = set()
all_internal_links = set()
def get_all_external_links(site_url):
    html = urlopen(site_url)
    soup = bs(html.read(),'lxml')
    internal_links = get_internal_links(soup, split_address(site_url)[0])
    external_links = get_external_links(soup, split_address(site_url)[0])
    
    for link in external_links:
        if link not in all_external_links:
            all_external_links.add(link)
            print link
    
    for link in internal_links:
        if link not in all_internal_links:
            print "------------------\n About to get link: " + link # drive a layer deeper
            all_internal_links.add(link)
            get_all_external_links(link)

get_all_external_links('http://oreilly.com')
            











               