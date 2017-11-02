# 爬取flickr图像描述的爬虫

## Flickr数据集

&ensp;&ensp;&ensp;`Flickr`是一个图像数据集，其中有很多图像，每张图像有五条描述。`Flickr`有两个数据集：

* Flickr8k
* Flickr30k

&ensp;&ensp;&ensp;数据样例如下:

&ensp;&ensp;&ensp;图像：

![exp](https://github.com/BlasphemyAngels/CrawlFickrData/blob/master/exp.png?raw=true)

&ensp;&ensp;&ensp;描述：

* A boy sand surfing down a hill
* A man is attempting to surf down a hill made of sand on a sunny day.
* A man is sliding down a huge sand dune on a sunny day.
* A man is surfing down a hill of sand.
* A young man in shorts and t-shirt is snowboarding under a bright blue sky.

&ensp;&ensp;&ensp;现在就爬取Flickr8k的数据集。

## 正文

&ensp;&ensp;&ensp;数据所在网站:[Flickr8k](http://nlp.cs.illinois.edu/HockenmaierGroup/8k-pictures.html)

### 环境

* python
* scrapy

### 运行

&ensp;&ensp;&ensp;进入第一层`CrawlFlickr`目录，此时所在目录跟文件`scrapy.cfg`同级，然后运行代码`scrapy crawl ImageText`即可。

### 原理

&ensp;&ensp;&ensp;关于`scrapy`的内容看博客[scrapy初涉](blasphemyangels.github.io/2017/07/17/2017-07-17-scrapystart/)即可。
