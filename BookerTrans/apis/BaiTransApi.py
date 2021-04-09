# coding: utf-8

import requests
import execjs
import json
import sys
from os import path

class BaiTransApi:

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    cookies = {
        "BAIDUID": "E5BB6C7348B207E45C3486FEEF987D2B:FG=1",
        "BIDUPSID": "E5BB6C7348B207E45C3486FEEF987D2B",
        "PSTM=1550637262": "MCITY=-50%3A276%3A315%3A78%3A46%3A",
        "REALTIME_TRANS_SWITCH=1": "FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1",
        "SOUND_SPD_SWITCH=1": "SOUND_PREFER_SWITCH=1",
        "_cfduid": "d626a3b24ca7e86a65862420b8b23e2281557130322",
        "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
        "Hm_lvt_64ecd82404c51e03dc91cb9e8c025574": "1562247416,1562248667,1562251219,1562287161",
        "Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574": "1562287161",
        "yjs_js_security_passport": "c871d63ce773ff4ae1c58367d3b75c8ee59b8d77_1562287161_js",
    }

    def __init__(self):
        js_name = path.join(path.dirname(__file__), "BaiTransTk.js")
        with open(js_name, encoding="utf-8") as f:
            self._js = execjs.compile(f.read())
        self.proxy = None
        self.timeout = 8

        
    def sign(self, s):
        return self._js.call("e", s)

    def translate(self, s, src='en', dst='zh'):
        if src == 'auto': src = 'en'
        if dst == 'zh-CN': dst = 'zh'
        data = {
            "from": src,
            "to": dst,
            "query": s,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": self.sign(s),
            "token": "b01862bd6d087dbdb2dd562ecd940435" 
        }
        j = requests.post(
            "https://fanyi.baidu.com/v2transapi", 
            data,
            headers=BaiTransApi.headers,
            cookies=BaiTransApi.cookies,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        return j["trans_result"]["data"][0]["dst"]
        

if __name__ == '__main__':
    api = BaiTransApi()
    while True:
        totrans = input("请输入你要翻译的内容")
        transed = api.translate(totrans)
        print(transed)