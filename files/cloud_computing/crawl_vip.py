"""
@Author: yanzx
@Date: 2022/7/3 11:35
@Description: 
"""
import time

url_f = "http://www.vipveg.com/price/2022/all/m6d-1cta-1by-1p{}.html"
# !/usr/bin/env python
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


if __name__ == '__main__':
    f = open("./vegetable.log", "a", encoding="utf-8")
    for j in range(1, 201):
        url = url_f.format(str(j))
        response = Response(url)
        html = response.analy()
        table = html.xpath("//table[2]//tr[position()>2]")
        for i in table:  # 遍历tr列表
            p = ''.join(i.xpath(".//td[1]//text()"))  # 获取当前tr标签下的第一个td标签，并用text()方法获取文本内容，赋值给p
            sl = ''.join(i.xpath(".//td[2]//text()"))
            sc = ''.join(i.xpath(".//td[3]//text()"))
            ll = ''.join(i.xpath(".//td[4]//text()"))
            lc = ''.join(i.xpath(".//td[5]//text()"))
            year = ''.join(i.xpath(".//td[6]//text()"))

            #     print(p, sl, sc, ll, lc, year)
            data = {  # 用数据字典，存储需要的信息
                'varity': ''.join(p.split()),  # .split()方法在此处作用是除去p中多余的空格 '\xa0'
                'market': ''.join(sl.split()),
                'price_min': ''.join(sc.split()).replace('￥', ''),
                'price_max': ''.join(ll.split()).replace('￥', ''),
                'price_average': ''.join(lc.split()).replace('￥', ''),
                'date': year
            }

            query_log = "{date} {varity} {market} {price_min} {price_max} {price_average}".format(
                date=data.get('date'),
                varity=data.get('varity'),
                market=data.get('market').replace('.', ''),
                price_min=data.get('price_min'),
                price_max=data.get('price_max'),
                price_average=data.get('price_average'))

            f.write(query_log + "\n")
        print(f"爬取第{j}页完成, url: {url}")
        time.sleep(1)
