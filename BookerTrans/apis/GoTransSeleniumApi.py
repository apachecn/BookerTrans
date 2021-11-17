from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class GoTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'default_url': 'https://translate.google.cn/?sl=auto&tl=zh-CN',
            'url_temp': 'https://translate.google.cn/?sl={src}&tl={dst}',
            'src_sel': 'textarea',
            'src_attr': 'value',
            'dst_sel': 'html>body>c-wiz>div>div:nth-of-type(2)>c-wiz>div:nth-of-type(2)>c-wiz>div:nth-of-type(1)>div:nth-of-type(2)>div:nth-of-type(2)>c-wiz:nth-of-type(2)>div:nth-of-type(5)>div>div:nth-of-type(1)>span:nth-of-type(1)',
            'dst_attr': 'innerText',
        }

def main():
    api = GoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()