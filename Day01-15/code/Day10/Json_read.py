# encoding: utf-8
"""
@version: 1.0
@author: 
@file: Json_read
@time: 2020-03-29 22:41
"""
import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()