from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class SoTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'url_temp': 'https://fanyi.sogou.com/text?transfrom={src}&transto={dst}',
            'src_text': '#trans-input',
            'dst_text': '#trans-result',
        }

def main():
    api = SoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()