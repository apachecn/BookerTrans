import requests
import json

class BingTransApi:
    
    headers = {
        'Origin': 'https://cn.bing.com',
        'Referer': 'https://cn.bing.com/translator/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    }
    
    def __init__(self):
        self.proxy = None
        self.timeout = 8
        
    def translate(self, s, src='en', dst='zh-Hans'):
        if src == 'auto': src = 'en'
        if dst == 'zh' or dst == 'zh-CN':
            dst = 'zh-Hans'
        data = {
            'fromLang': src,
            'to': dst,
            'text': s,
        }
        j = requests.post(
            'https://cn.bing.com/ttranslatev3',
            data=data,
            headers=BingTransApi.headers,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        return j[0]['translations'][0]['text']
        
if __name__ == '__main__': 
    api = BingTransApi()
    transed = api.translate(input('请输入待翻译文本'))
    print(transed)