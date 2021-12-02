from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class AliTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'default_url': 'https://translate.alibaba.com/',
            'url_temp': 'https://translate.alibaba.com/',
            'src_sel': 'textarea#source',
            'src_attr': 'value',
            'dst_sel': '.input-text pre',
            'dst_attr': 'innerText',
        }

def main():
    api = AliTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()