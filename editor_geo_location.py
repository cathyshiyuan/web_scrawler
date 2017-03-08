#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:54:59 2017

@author: Cathy
"""

from urllib import urlopen
from bs4 import BeautifulSoup as bs
import datetime
import random
import re
from urllib2 import HTTPError
import json

random.seed(datetime.datetime.now())

# https://en.wikipedia.org/w/index.php?title=Python&action=history
# https://en.wikipedia.org/wiki/Python

def get_links(item_name):
    html = urlopen('http://en.wikipedia.org' + item_name)
    soup = bs(html,'lxml')
    return soup.find('div', id = 'bodyContent').findAll('a',
                    href = re.compile("^(/wiki/)((?!:).)*$"))

def get_editor_ip(page_url):
    page_url = page_url.replace('/wiki/', '')
    history_url = ('https://en.wikipedia.org/w/index.php?title=' + 
                   page_url + '&action=history')
    print 'history url is: ' + history_url
    html = urlopen(history_url)
    soup = bs(html)
    ips = soup.findAll('a',{'class':"mw-userlink mw-anonuserlink"})
    ip_list = set()
    for ip in ips:
        ip_list.add(ip.get_text())
    return ip_list
    #return ips
#print get_editor_ip('/wiki/Python')


def get_location(ip):
    try:
        response = urlopen('http://freegeoip.net/json/' + ip).read().decode('utf-8')
    except HTTPError:
        return None
    response_json = json.loads(response)
    #infos = map(lambda x: response_json.get(x), keys)
    return [response_json.get('country_name'),
            response_json.get('city'),
            response_json.get('zip_code')]
    
links = get_links('/wiki/Python')
#print links[1].get_text()


id_counts = 0
while (id_counts < 10):
    for link in links:
        print '------------New Page---------------'
        editor_ips = get_editor_ip(link.attrs['href'])
        id_counts += 1
        for editor_ip in editor_ips:
            location = get_location(editor_ip)
            print "Editor IP is : " + editor_ip + '\nLocation is: '+ location[0],location[1],location[2]
    
    new_link = links[random.randint(0,len(links)-1)].attrs['href']
    links = get_links(new_link)
    

            













    
    