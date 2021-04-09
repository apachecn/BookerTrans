import requests
import re
import os
import json
from urllib.parse import quote
import sys

class GoTransApi:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }

    def __init__(self):
        self.tkk = None
        self.host = 'translate.google.cn'
        self.proxy = None
        self.timeout = 8
    
    @staticmethod
    def _shr32(x, bits):
        if bits <= 0:
            return x

        if bits >= 32:
            return 0

        x_bin = bin(x)[2:]
        x_bin_length = len(x_bin)

        if x_bin_length > 32:
            x_bin = x_bin[x_bin_length - 32: x_bin_length]

        if x_bin_length < 32:
            x_bin = x_bin.zfill(32)

        return int(x_bin[:32 - bits].zfill(32), 2)

    @staticmethod
    def _rl(a, b):
        for c in range(0, len(b) - 2, 3):
            d = b[c + 2]

            if d >= 'a':
                d = ord(d[0]) - 87
            else:
                d = int(d)

            if b[c + 1] == '+':
                d = GoTransApi._shr32(a, d)
            else:
                d = a << d

            if b[c] == '+':
                a = a + d & (2 ** 32 - 1)
            else:
                a = a ^ d

        return a

    def get_tk(self, a, tkk=None):
        if not tkk: tkk = self.get_tkk()
        tkk = tkk.split('.')
        
        b = int(tkk[0])
        d = []

        for f in range(0, len(a)):
            g = ord(a[f])

            if g < 128:
                d.append(g)
            else:
                if g < 2048:
                    d.append(g >> 6 | 192)
                else:
                    if ((g & 0xfc00) == 0xd800 and
                            f + 1 < len(a) and
                            (ord(a[f + 1]) & 0xfc00) == 0xdc00):

                        f += 1
                        g = 0x10000 + ((g & 0x3ff) << 10) + (ord(a[f]) & 0x3ff)

                        d.append(g >> 18 | 240)
                        d.append(g >> 12 & 63 | 128)
                    else:
                        d.append(g >> 12 | 224)
                        d.append(g >> 6 & 63 | 128)

                d.append(g & 63 | 128)

        a = b

        for e in range(0, len(d)):
            a += d[e]
            a = GoTransApi._rl(a, "+-a^+6")

        a = GoTransApi._rl(a, "+-3^+b+-f")

        a = a ^ int(tkk[1])

        if a < 0:
            a = (a & (2 ** 31 - 1)) + 2 ** 31

        a %= 10 ** 6

        return f"{a}.{a ^ b}"
        
    def get_tkk(self):
        return '422392.71207223'
        '''
        if not self.tkk: 
            res = requests.get(
                f'https://{self.host}/', 
                headers=GoTransApi.headers, 
                proxies=self.proxy,
                timeout=self.timeout,
            ).text
            self.tkk = re.search(r"tkk:'(\d+\.\d+)", res).group(1)
        return self.tkk
        '''

    
    def translate(self, s, src='auto', dst='zh-CN'):
        tk = self.get_tk(s)
        url = f'https://{self.host}/translate_a/single?' + \
              f'client=webapp&sl={src}&tl={dst}&dt=t&tk={tk}' + \
              f'&q={quote(s)}'
        res = requests.get(
            url, 
            headers=GoTransApi.headers, 
            proxies=self.proxy,
            timeout=self.timeout,
        ).text
        j = json.loads(res)
        trans = ' '.join([o[0] for o in j[0]])
        return trans

def main():
    cmd = sys.argv[1]
    if cmd not in ['tk', 'trans']:
        return
    text = sys.argv[2]
    api = GoTransApi()
    if cmd == 'tk':
        print(f"{text}: {api.get_tk(text)}")
    else:
        print(f"{text}: {api.translate(text)}")

if __name__ == '__main__': main()
