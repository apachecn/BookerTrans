# coding: utf-8

import os
from os import path
from argparse import ArgumentParser
from . import trans_html, config, api, __version__

is_html = lambda f: f.endswith('.html') or f.endswith('.htm')

def process_file(fname):
    if not is_html(fname):
        print(f'{fname} is not a html file')
        return
    
    print(fname)
    html = open(fname, encoding='utf-8').read()
    html = trans_html(html)
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

def process_dir(dir):
    files = [f for f in os.listdir(dir) if is_html(f)]
    for f in files:
        f = path.join(dir, f)
        process_file(f)

def main():
    parser = ArgumentParser(prog="BookerTrans", description="HTML Translator with Google Api for iBooker/ApacheCN")
    parser.add_argument('fname', help="html file name or dir name")
    parser.add_argument('-v', '--version', action="version", version=__version__)
    parser.add_argument('-H', '--host', default='translate.google.cn', help="host for google translator")
    parser.add_argument('-P', '--proxy', help=f'proxy with format \d+\.\d+\.\d+\.\d+:\d+ or empty')
    parser.add_argument('-t', '--timeout', type=float, help=f'timeout in second')
    parser.add_argument('-w', '--wait-sec', type=float, default=0.5, help='delay in second between two times of translation')
    parser.add_argument('-r', '--retry', type=int, default=10, help='count of retrying')
    parser.add_argument('-s', '--src', default='auto', help='src language')
    parser.add_argument('-d', '--dst', default='zh-CN', help='dest language')
    args = parser.parse_args()
    
    if args.proxy:
        p = args.proxy
        args.proxy = {'http': p, 'https': p}
    api.host = args.host
    api.proxy = args.proxy
    api.timeout = args.timeout
    config.wait_sec = args.wait_sec
    config.retry = args.retry
    config.src = args.src
    config.dst = args.dst

    if path.isdir(args.fname):
        process_dir(args.fname)
    else:
        process_file(args.fname)
        
if __name__ == '__main__': main()
