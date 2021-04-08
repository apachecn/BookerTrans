from .GoTransApi import GoTransApi
from .GoTransSeleniumApi import GoTransSeleniumApi

apis = {
    'google': GoTransApi,
    'google_selenium': GoTransSeleniumApi,
}