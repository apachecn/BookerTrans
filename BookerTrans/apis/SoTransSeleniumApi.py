from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class SoTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'url_temp': 'https://fanyi.sogou.com/text?transfrom={src}&transto={dst}',
            'src_sel': '#trans-input',
            'src_attr': 'value',
            'dst_sel': '#trans-result',
            'dst_attr': 'innerText',
        }

def main():
    api = SoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()