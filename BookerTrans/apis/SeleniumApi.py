from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys

class SeleniumApi:

    def get_settings(self):
        return {
            'url_temp': '',
            'src_text': '',
            'dst_text': '',
        }

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        self._driver = webdriver.Chrome(options=options)
        self._driver.get(self.get_settings()['url_temp']
            .replace('{src}', 'auto')
            .replace('{dst}', 'zh-CN'))
        self._lang = ('auto', 'zh-CN')

    def translate(self, s, src='auto', dst='zh-CN'):
        settings = self.get_settings()
        if self._lang != (src, dst):
            self._driver.get(settings['url_temp']
                .replace('{src}', src)
                .replace('{dst}', dst))
            self._lang = (src, dst)
        text_dummy = self._driver \
            .find_element_by_css_selector(settings['src_text'])
        text_dummy.clear()
        text_dummy.send_keys(s)
        time.sleep(1)
        text_translation = self._driver \
            .find_element_by_css_selector(settings['dst_text'])
        return text_translation.text

    def __del__(self):
        self._driver.close()
