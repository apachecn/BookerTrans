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

## 使用说明

```
btrans [-h] [-v] [-H HOST] [-P PROXY] [-w WAIT_SEC] [-r RETRY]
       [-s SRC] [-d DST]
       fname
       
-H HOST: 域名，默认为 translate.google.com
-P PROXY: 代理，格式为 \d+\.\d+\.\d+\.\d+:\d+，默认为空
-w WAIT_SEC: 两次翻译之间的延迟（以秒为单位）
-r RETRY: 重试次数
-s SRC: 源语言，默认为 auto
-d DST: 目标语言，默认为 zh-CN
fname: HTML 文件名称，文件所在的目录名称
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
