from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi
from .SoTransSeleniumApi import SoTransSeleniumApi
from .YoudaoTransSeleniumApi import YoudaoTransSeleniumApi
from .BaiTransApi import BaiTransApi
from .YoudaoTransApi import YoudaoTransApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
    'baidu': BaiTransApi,
    'baidu_selenium': BaiTransSeleniumApi,
    'sogou': SoTransSeleniumApi,
    'youdao': YoudaoTransApi,
    'youdao_selenium': YoudaoTransSeleniumApi,
}