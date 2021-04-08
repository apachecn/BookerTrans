from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi
from .SoTransSeleniumApi import SoTransSeleniumApi
from .YoudaoTransSeleniumApi import YoudaoTransSeleniumApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
    'baidu': BaiTransSeleniumApi,
    'sogou': SoTransSeleniumApi,
    'youdao': YoudaoTransSeleniumApi,
}