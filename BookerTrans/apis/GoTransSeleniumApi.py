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
            'src_sel': 'textarea[role=combobox]',
            'src_attr': 'value',
            'dst_sel': 'span[lang=zh-CN]',
            'dst_attr': 'innerText',
        }

def main():
    api = GoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()