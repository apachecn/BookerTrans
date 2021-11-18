import time
import random
from hashlib import md5
import requests
import json
import uuid
 
class SoTransApi:
 
    headers = {
        'Origin': "https://fanyi.sogou.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
        'Accept': "application/json, text/plain, */*",
        'X-Requested-With': "XMLHttpRequest",
        'Referer': "https://fanyi.sogou.com/text",
    }
 
    def __init__(self):
        self.proxy = None
        self.timeout = 8
 
 
    def translate(self, s, src='auto', dst='zh-CHS'):
        if dst == 'zh-CN': dst = 'zh-CHS'
        sign_str = src + dst + s + "109984457"
        sign = md5(sign_str.encode("utf-8")).hexdigest()
 
        data = {
            "client": "pc",
            "exchange": False,
            "fr": "browser_pc",
            "from": src,
            "needQc": 1,
            "s": sign,
            "text": s,
            "to": dst,
            "uuid": uuid.uuid4().hex,
        }
 
        j = requests.post(
            "https://fanyi.sogou.com/api/transpc/text/result", 
            data=data, 
            headers=SoTransApi.headers,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        if j['info'] != 'success':
            raise Exception(json.dumps(j))
        return j['data']['translate']['dit']
 
if __name__ == "__main__":
    api = SoTransApi()
    transed = api.translate(input("请输入待翻译文本"))
    print(transed)