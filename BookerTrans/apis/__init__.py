from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi
from .SoTransSeleniumApi import SoTransSeleniumApi
from .YoudaoTransSeleniumApi import YoudaoTransSeleniumApi
from .BaiTransApi import BaiTransApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
    'baidu': BaiTransApi,
    'baidu_selenium': BaiTransSeleniumApi,
    'sogou': SoTransSeleniumApi,
    'youdao': YoudaoTransSeleniumApi,
}