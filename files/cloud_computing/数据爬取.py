#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import urllib.request
import urllib.parse
from lxml import etree


class Response:
    def __init__(self, url, data=None):
        self.url = url
        self.data = data
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Mobile Safari/537.36"}

    def urllib_req(self):
        if self.data:
            data = bytes(urllib.parse.urlencode(self.data), encoding='utf-8')
            req = urllib.request.Request(url=self.url, headers=self.headers, data=data)
            response = urllib.request.urlopen(req)
            return response
        else:
            req = urllib.request.Request(url=self.url, headers=self.headers)
            response = urllib.request.urlopen(req)
            return response

    def requests_req(self):
        if self.data:
            response = requests.post(url=self.url, headers=self.headers, data=self.data)
            response.encoding = 'utf-8'
            return response
        else:
            response = requests.get(url=self.url, headers=self.headers)
            response.encoding = 'utf-8'
            return response

    def analy(self):
        html = etree.HTML(self.requests_req().text)
        return html


f = open("data/vegetable.log", "w+")
for page in range(100, 1, -1):
    url = 'http://www.vegnet.com.cn/Price/List_ar500000_p' + str(page) + '.html?marketID=0'
    response = Response(url)
    html = response.analy()
    info = html.xpath('//div[@class="pri_k"]/p')
    for i in info:
        date = i.xpath('./span[1]/text()')[0][1:][:-1]
        varity = i.xpath('./span[2]/text()')[0]
        market = i.xpath('./span[3]/a/text()')[0]
        price_min = i.xpath('./span[4]/text()')[0][1:]
        price_max = i.xpath('./span[5]/text()')[0][1:]
        price_average = i.xpath('./span[6]/text()')[0][1:]
        unit = i.xpath('./span[7]/text()')[0]
        query_log = "{date} {varity} {market} {price_min} {price_max} {price_average} {unit} ".format(date=date,
                                                                                                      varity=varity,
                                                                                                      market=market,
                                                                                                      price_min=price_min,
                                                                                                      price_max=price_max,
                                                                                                      price_average=price_average,
                                                                                                      unit=unit)
        f.write(query_log + "\n")


        print("main")
        print("main")


        print("local")
        print("local")