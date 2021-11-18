import requests
import json
import time

class QTransApi:
    
    headers = {
        'Origin': 'https://fanyi.qq.com',
        'Referer': 'https://fanyi.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    }
    
    def __init__(self):
        self._tk = None
        self.proxy = None
        self.timeout = 8
        
    def reauth(self):
        j = requests.post(
            'https://fanyi.qq.com/api/reauth12f',
            headers=QTransApi.headers,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        return j
        
    def translate(self, s, src='auto', dst='zh-CN'):
        if not self._tk:
            self._tk = self.reauth()
            
        headers = QTransApi.headers.copy()
        headers['Cookie'] = 'qtv={}; qtk={}'.format(
            self._tk['qtv'], self._tk['qtk'])
            
        data = {
            'source': src,
            'target': dst,
            'sourceText': s,
            'qtv': self._tk['qtv'],
            'qtk': self._tk['qtk'],
            'sessionUuid': 'translate_uuid' + str(int(time.time() * 1000))
        }
        
        j = requests.post(
            'https://fanyi.qq.com/api/translate',
            data=data,
            headers=headers,
            proxies=self.proxy,
            timeout=self.timeout,
        ).json()
        if j['errCode'] != 0:
            raise Exception(j['errMsg'])
        return ' '.join([
            r['targetText'] 
            for r in j['translate']['records']
        ])
        
if __name__ == '__main__': 
    api = QTransApi()
    transed = api.translate(input('请输入待翻译文本'))
    print(transed)