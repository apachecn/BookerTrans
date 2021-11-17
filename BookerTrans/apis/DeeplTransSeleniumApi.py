from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class DeeplTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'default_url': 'https://www.deepl.com/translator#en/zh-CN/',
            'url_temp': 'https://www.deepl.com/translator#{src}/{dst}/',
            'src_sel': '.lmt__source_textarea',
            'src_attr': 'value',
            'dst_sel': '#target-dummydiv',
            'dst_attr': 'innerHTML',
        }

def main():
    api = DeeplTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()