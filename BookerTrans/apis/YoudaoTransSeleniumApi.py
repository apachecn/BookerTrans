from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class YoudaoTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'url_temp': 'http://fanyi.youdao.com/',
            'src_sel': '#inputOriginal',
            'src_attr': 'value',
            'dst_sel': '#transTarget',
            'dst_attr': 'innerText',
        }

def main():
    api = YoudaoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()