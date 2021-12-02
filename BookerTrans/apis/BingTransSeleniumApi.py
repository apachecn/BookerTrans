from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class BingTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'default_url': 'https://cn.bing.com/translator/',
            'url_temp': 'https://cn.bing.com/translator/',
            'src_sel': 'textarea#tta_input_ta',
            'src_attr': 'value',
            'dst_sel': 'textarea#tta_output_ta',
            'dst_attr': 'value',
        }

def main():
    api = BingTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()