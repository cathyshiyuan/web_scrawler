#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import json
import pandas as pd
from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup as bs



key = 'TEF4w26OXp39iRQZjSL5qRgyFORAZzM4'
df = pd.read_csv('/Users/Cathy 1/Desktop/get_poi/fixed_hangzhou.csv')

for n, i in enumerate(df.latlon[:5]):
	lng = i.split(',')[0]
	lat = i.split(',')[1]
	#print lng, lat
	url = 'http://api.map.baidu.com/place/v2/search?query=$汽车$医疗$酒店$美食$休闲$娱乐$购物$金融$&scope=2&output=json&location=%s,%s&radius=100&filter=sort_name:distance|sort_rule:1&ak=TEF4w26OXp39iRQZjSL5qRgyFORAZzM4'%(lat,lng)
	#print url
	try:
		data = json.load(urllib2.urlopen(url))
		print '==================================================================================================================================================='
		print 'Baidu Raw Data:', 'Name:', df.ix[n,'Name'], '\t', 'Address:', df.ix[n, 'Address'], '\t', 'Baidu Latlng:',df.ix[n, 'latlon'], '\t', 'Tags:', df.ix[n, 'tag'], '\t', 'scn_id:',df.ix[n, 'scn_id']
		for i in data['results']:
			
			print 'Name:',i['name'],'\t','Address:',i['address'],'\t','Baidu Latlng',i['location'],'\t','Tags:',i['detail_info']['tag'], 'Distance:',i['detail_info']['distance']+'m∫'
	except:
		print 'HTTP Error 400: Bad Request','Name:', df.ix[n,'Name'], '\t', 'Address:', df.ix[n, 'Address'], '\t', 'Baidu Latlng:',df.ix[n, 'latlon']
