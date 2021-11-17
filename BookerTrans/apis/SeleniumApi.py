from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import re

class SeleniumApi:

    WAIT_SEC = 10000000
    
    def get_settings(self):
        return {
            'url_temp': '',
            'src_text': '',
            'dst_text': '',
        }

    def load_page(self, src='auto', dst='zh-CN'):
        settings = self.get_settings()
        self._driver.get(settings['url_temp']
            .replace('{src}', src)
            .replace('{dst}', dst))
        self._driver.implicitly_wait(SeleniumApi.WAIT_SEC)
        self._lang = (src, dst)
        
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        self._driver = webdriver.Chrome(options=options)
        self.load_page('auto', 'zh-CN')

    def wait_trans_callback(self, dvr):
        settings = self.get_settings()
        el_dst = dvr.find_element_by_css_selector(settings['dst_text'])
        return el_dst is not None and el_dst.text != ""

    def translate(self, s, src='auto', dst='zh-CN'):
        if re.search(r'^\s*$', s): return ""
        settings = self.get_settings()
        if self._lang != (src, dst):
            self.load_page(src, dst)
        el_src = self._driver \
            .find_element_by_css_selector(settings['src_text'])
        el_src.clear()
        WebDriverWait(self._driver, SeleniumApi.WAIT_SEC) \
            .until(lambda x: not self.wait_trans_callback(x))
        el_src.send_keys(s)
        WebDriverWait(self._driver, SeleniumApi.WAIT_SEC) \
            .until(self.wait_trans_callback)
        el_dst = self._driver \
            .find_element_by_css_selector(settings['dst_text'])
        return el_dst.text

    def __del__(self):
        self._driver.close()
