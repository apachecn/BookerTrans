# coding: utf-8

import re
import time
from os import path
from pyquery import PyQuery as pq
from .apis import apis
from . import config

__author__ = "ApacheCN"
__email__ = "apachecn@163.com"
__license__ = "SATA"
__version__ = "2021.4.9.2"

RE_CODE = r'<(pre|code|tt|var|kbd)[^>]*?>[\s\S]*?</\1>'
RE_TAG = r'<[^>]*?>'
RE_ENTITY = r'&(\w+|#x?\d+);'

api = None

def load_api(site):
    global api
    api = apis[site]()
    
def get_api():
    return api

def tags_preprocess(html):

    '''
    # 去头去尾
    html = html.replace("<?xml version='1.0' encoding='utf-8'?>", '')
    html = re.sub(r'<html[^>]*?>.*?<body[^>]*?>', '', html, flags=re.RegexFlag.DOTALL)
    html = re.sub(r'</body>.*?</html>', '', html, flags=re.RegexFlag.DOTALL)
    '''
    
    tags = []
    
    def replace_func(m):
        s = m.group()
        tags.append(s)
        idx = len(tags) - 1
        tk = f'\x20【T{idx}】\x20'
        return tk
        
    # 移除 <pre|code>
    html = re.sub(RE_CODE, replace_func, html)
    # 移除其它标签
    html = re.sub(RE_TAG, replace_func, html)
    # 移除实体
    html = re.sub(RE_ENTITY, replace_func, html)
    
    # 去掉 Unix 和 Windows 换行
    html = html.replace('\n', ' ')
    html = html.replace('\r', '')
    return html, tags

def tags_recover(html, tags):

    # 还原标签
    for i, t in enumerate(tags):
        html = html.replace(f'【T{i}】', t)
        
    return html

def trans_real(src):

    dst = None
    for i in range(config.retry):
        try:
            print(src)
            dst = api.translate(
                src, 
                src=config.src, 
                dst=config.dst
            )
            print(dst)
            time.sleep(config.wait_sec)
            if dst: break
        except Exception as ex:
            print(ex)
            time.sleep(config.wait_sec)
    
    if not dst: return None
    
    # 修复占位符
    dst = re.sub(r'【\s*T\s*(\d+)\s*】', r'【T\1】', dst, flags=re.I)
    return dst

def trans_one(html):
    if html is None or html.strip() == '':
        return ''
    
    # 标签预处理
    html, tokens = tags_preprocess(html)
    
    # 按句子翻译
    html = trans_real(html)
    if not html: return None
    
    # 标签还原
    html = tags_recover(html, tokens)
    return html

def trans_html(html):
    # 预处理
    html = preprocess(html)
    root = pq(html)
    
    # 处理 <p> <h?>
    elems = root('p, h1, h2, h3, h4, h5, h6')
    for elem in elems:
        elem = pq(elem)
        to_trans = elem.html()
        trans = trans_one(to_trans)
        if not trans: continue
        elem.html(trans)
        
    # 处理 <blockquote> <td> <th>
    elems = root('blockquote, td, th')
    for elem in elems:
        elem = pq(elem)
        if elem.children('p'): continue
        to_trans = elem.html()
        trans = trans_one(to_trans)
        if not trans: continue
        elem.html(trans)
    
    # 处理 <li>
    elems = root('li')
    for elem in elems:
        elem = pq(elem)
        if elem.children('p'): continue
        
        # 如果有子列表，就取下来
        sub_list = None
        if elem.children('ul'): sub_list = elem.children('ul')
        if elem.children('ol'): sub_list = elem.children('ol')
        if sub_list: sub_list.remove()
        
        to_trans = elem.html()
        trans = trans_one(to_trans)
        if not trans: continue
        elem.html(trans)
        
        # 将子列表还原
        if sub_list: elem.append(sub_list)
    
    return str(root)

def preprocess(html):
    html = re.sub(r'<\?xml[^>]*\?>', '', html)
    html = re.sub(r'xmlns=".+?"', '', html)
    html = html.replace('&#160;', ' ') \
               .replace('&nbsp;', ' ')

    root = pq(html)
    
    pres = root('div.code, div.Code')
    for p in pres:
        p = pq(p)
        newp = pq('<pre></pre>')
        newp.append(p.text())
        p.replace_with(newp)
        
    codes = root('span.inline-code, span.CodeInline')
    for c in codes:
        c = pq(c)
        newc = pq('<code></code>')
        newc.append(c.text)
        c.replace_with(newc)
        
    return str(root)

