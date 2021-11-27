from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi
from .SoTransSeleniumApi import SoTransSeleniumApi
from .SoTransApi import SoTransApi
from .YoudaoTransSeleniumApi import YoudaoTransSeleniumApi
from .BaiTransApi import BaiTransApi
from .YoudaoTransApi import YoudaoTransApi
from .QTransApi import QTransApi
from .QTransSeleniumApi import QTransSeleniumApi
from .BingTransApi import BingTransApi
from .DeeplTransSeleniumApi import DeeplTransSeleniumApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
    'baidu': BaiTransApi,
    'baidu_selenium': BaiTransSeleniumApi,
    'sogou': SoTransApi,
    'sogou_selenium': SoTransSeleniumApi,
    'youdao': YoudaoTransApi,
    'youdao_selenium': YoudaoTransSeleniumApi,
    'qq': QTransApi,
    'qq_selenium': QTransSeleniumApi,
    'bing': BingTransApi,
    'deepl': DeeplTransSeleniumApi,
}