#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests        #导入requests包
import json
def get_translate_date(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    From_data={'i': '我爱中国','from': 'AUTO','to': 'AUTO','smartresult': 'dict','client': 'fanyideskweb','salt': '15686180794930','sign': 'fc1befa2f02959c642feccd65936c99c','ts': '1568618079493','bv': '37074a7035f34bfbf10d32bb8587564a','doctype': 'json','version': '2.1','keyfrom': 'fanyi.web','action': 'FY_BY_CLICKBUTTION'}
    #请求表单数据
    response = requests.post(url,data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
if __name__=='__main__':
    get_translate_date('我爱中国')