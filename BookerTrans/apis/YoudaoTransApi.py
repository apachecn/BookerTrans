import time
import random
from hashlib import md5
import requests
import json
 
class YoudaoTransApi:
 
    headers = {
        'Origin': "http://fanyi.youdao.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': "http://fanyi.youdao.com/",
        'Cookie': "OUTFOX_SEARCH_USER_ID=-{0}@{1}.{2}.{3}.{4}; ".format(
            str(random.randint(100000000,999999999)), 
            str(random.randint(10, 241)), 
            str(random.randint(10, 241)), 
            str(random.randint(10, 241)), 
            str(random.randint(10, 241)),
        ),
    }
 
    def __init__(self):
        self.proxy = None
        self.timeout = 8
 
 
    def translate(self, s, src='auto', dst='zh-CN'):
        salt = str(int(time.time()*1000)) +str(random.randint(0,9))
        sign_str = "fanyideskweb" + s + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        sign = md5(sign_str.encode("utf-8")).hexdigest()
 
        data = {
            "i": s,
            "from": src,
            "to": dst,
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false"
        }
 
        j = requests.post(
            "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule", 
            data=data, 
            headers=YoudaoTransApi.headers,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        return j["translateResult"][0][0]["tgt"]
 
if __name__ == "__main__":
    api = YoudaoTransApi()
    transed = api.translate(input("请输入待翻译文本"))
    print(transed)