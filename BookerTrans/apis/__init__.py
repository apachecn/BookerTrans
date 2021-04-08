from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi
from .BaiTransSeleniumApi import BaiTransSeleniumApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
    'baidu': BaiTransSeleniumApi,
}