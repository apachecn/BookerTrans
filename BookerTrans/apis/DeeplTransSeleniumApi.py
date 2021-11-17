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
            'src_text': '.lmt__source_textarea',
            'dst_text': '#target-dummydiv',
        }

def main():
    api = DeeplTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()