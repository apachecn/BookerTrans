from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
from .SeleniumApi import SeleniumApi

class BaiTransSeleniumApi(SeleniumApi):

    def get_settings(self):
        return {
            'default_url': 'https://fanyi.baidu.com/#auto/zh-CN',
            'url_temp': 'https://fanyi.baidu.com/#{src}/{dst}',
            'src_sel': 'textarea.textarea',
            'src_attr': 'value',
            'dst_sel': 'p.target-output',
            'dst_attr': 'innerText',
        }

def main():
    api = BaiTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()