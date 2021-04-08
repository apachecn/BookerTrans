from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

class GoTransSeleniumApi:

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        self._driver = webdriver.Chrome(options=options)
        # 打开谷歌翻译
        self._driver.get('https://translate.google.cn/?sl=auto&tl=zh-CN')
        self._lang = ('auto', 'zh-CN')

    def translate(self, s, src='auto', dst='zh-CN'):
        if self._lang != (src, dst):
            self._driver.get(f'https://translate.google.cn/?sl={src}&tl={dst}')
            self._lang = (src, dst)
        # 获取文本输入域
        text_dummy = self._driver.find_element_by_css_selector('textarea')
        text_dummy.clear()
        text_dummy.send_keys(s)
        time.sleep(1)
        text_translation = self._driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]/span[1]')
        # 返回翻译结果
        return text_translation.text

    def __del__(self):
        self._driver.close()

def main():
    api = GoTransSeleniumApi()
    print(api.translate(sys.argv[1]))
    
if __name__ == '__main__': main()