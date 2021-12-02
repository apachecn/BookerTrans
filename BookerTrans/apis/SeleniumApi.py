from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import time
import sys
import re
from ..config import config

class SeleniumApi:

    WAIT_SEC = 10
    
    def get_settings(self):
        return {
            'url_temp': '',
            'src_sel': '',
            'src_attr': 'value',
            'dst_sel': '',
            'dst_attr': 'innerText',
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
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        if config['debug']:
            options.add_argument('--log-level=3')
        else:
            options.add_argument('--headless')
            options.add_argument('--log-level=0')
        self._driver = webdriver.Chrome(options=options)
        self.load_page('auto', 'zh-CN')

    def wait_trans_callback(self, dvr):
        settings = self.get_settings()
        res = self._driver.execute_script('''
            var el_dst = document.querySelector(arguments[0])
            return el_dst && el_dst[arguments[1]] != ""
        ''', settings['dst_sel'], settings['dst_attr'])
        return res

    def translate(self, s, src='auto', dst='zh-CN'):
        if re.search(r'^\s*$', s): return ""
        settings = self.get_settings()
        # if self._lang != (src, dst):
        self.load_page(src, dst)
        self._driver.refresh()
        # 清除输入框
        # self._driver.execute_script('''
            # var el_src = document.querySelector(arguments[0])
            # el_src[arguments[1]] = ''
            # el_src.dispatchEvent(new Event('input', {bubbles: true}))
        # ''', settings['src_sel'], settings['src_attr'])
        # 清除输出框
        # self._driver.execute_script('''
            # var el_dst = document.querySelector(arguments[0])
            # if (el_dst) el_dst[arguments[1]] = ''
        # ''', settings['dst_sel'], settings['dst_attr'])
        # 输入待翻译文本
        self._driver.execute_script('''
            var el_src = document.querySelector(arguments[0])
            el_src[arguments[1]] = arguments[2]
            el_src.dispatchEvent(new Event('input', {bubbles: true}))
        ''', settings['src_sel'], settings['src_attr'], s)
        # 等待反应
        WebDriverWait(self._driver, SeleniumApi.WAIT_SEC) \
            .until(self.wait_trans_callback)
        # 获取结果
        transed = self._driver.execute_script('''
            var el_dst = document.querySelectorAll(arguments[0])
            return Array.from(el_dst)
                .map(x => x[arguments[1]])
                .join(' ')
        ''', settings['dst_sel'], settings['dst_attr'])
        return transed

    def __del__(self):
        self._driver.close()
