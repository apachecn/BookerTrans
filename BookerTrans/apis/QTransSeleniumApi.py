from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class QTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'url_temp': 'https://fanyi.qq.com/',
            'src_sel': '.textpanel-source textarea.textinput',
            'src_attr': 'value',
            'dst_sel': '.text-dst',
            'dst_attr': 'innerText',
        }

def main():
    api = QTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()