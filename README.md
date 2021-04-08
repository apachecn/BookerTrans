# BookerTrans

用于 iBooker/ApacheCN 翻译项目的 HTML 谷歌翻译工具

## 安装

通过pip（推荐）：

```
pip install BookerTrans
```

从源码安装：

```
pip install git+https://github.com/apachecn/BookerTrans
```

部分 API 依赖 Selenium 和 Chrome。请确保安装了 Chrome，并将其[驱动](http://npm.taobao.org/mirrors/chromedriver/)放到`PATH`下。

## 使用说明

```
btrans [-h] [-v] [-H HOST] [-P PROXY] [-t TIMEOUT] [-w WAIT_SEC] 
       [-r RETRY] [-s SRC] [-d DST]
       site fname
       
-H HOST: 域名，默认为 translate.google.com
-P PROXY: 代理，格式为 \d+\.\d+\.\d+\.\d+:\d+，默认为空
-t TIMEOUT: 超时时间，以秒为单位，默认为 8
-w WAIT_SEC: 两次翻译之间的延迟（以秒为单位），默认为 0.5
-r RETRY: 重试次数，默认为 10
-s SRC: 源语言，默认为 auto
-d DST: 目标语言，默认为 zh-CN
site: API 名称，可选项为 {google,google_selenium,baidu,sogou,youdao}
fname: HTML 文件名称，或者文件所在的目录名称
```

## 协议

本项目基于 SATA 协议发布。

您有义务为此开源项目点赞，并考虑额外给予作者适当的奖励。

## 赞助我们

![](https://home.apachecn.org/img/about/donate.jpg)

## 另见

+   [ApacheCN 学习资源](https://docs.apachecn.org/)
+   [计算机电子书](http://it-ebooks.flygon.net)
+   [布客新知](http://flygon.net/ixinzhi/)
