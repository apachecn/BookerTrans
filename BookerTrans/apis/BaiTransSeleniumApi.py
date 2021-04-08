from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

class BaiTransSeleniumApi:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://fanyi.baidu.com/#auto/zh-CN')
        self._lang = ('auto', 'zh-CN')

    def translate(self, s, src='auto', dst='zh-CN'):
        if self._lang != (src, dst):
            self._driver.get(f'https://fanyi.baidu.com/#{src}/{dst}')
            self._lang = (src, dst)
        text_dummy = self._driver.find_element_by_css_selector('textarea.textarea')
        text_dummy.clear()
        text_dummy.send_keys(s)
        time.sleep(1)
        text_translation = self._driver.find_element_by_css_selector('p.target-output')
        return text_translation.text

    def __del__(self):
        self._driver.close()

def main():
    api = BaiTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()