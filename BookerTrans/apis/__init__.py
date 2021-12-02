from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi
from .SoTransSeleniumApi import SoTransSeleniumApi
from .YoudaoTransSeleniumApi import YoudaoTransSeleniumApi
from .YoudaoTransApi import YoudaoTransApi
from .QTransSeleniumApi import QTransSeleniumApi
from .DeeplTransSeleniumApi import DeeplTransSeleniumApi

apis = {
    'google_selenium': GoTransSeleniumApi,
    'baidu_selenium': BaiTransSeleniumApi,
    'sogou_selenium': SoTransSeleniumApi,
    'youdao': YoudaoTransApi,
    'youdao_selenium': YoudaoTransSeleniumApi,
    'qq_selenium': QTransSeleniumApi,
    'deepl': DeeplTransSeleniumApi,
}