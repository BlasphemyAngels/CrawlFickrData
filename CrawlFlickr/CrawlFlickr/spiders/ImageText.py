# -*- coding: utf-8 -*-
import os
import scrapy
from CrawlFlickr.items import FlickrItem


class ImagetextSpider(scrapy.Spider):
    name = 'ImageText'
    start_urls = [
        'http://nlp.cs.illinois.edu/HockenmaierGroup/8k-pictures.html']

    def __init__(self):
        if not os.path.exists("data/"):
            os.system("mkdir data")

    def parse(self, response):
        base = 160000
        num = 0
        content = response.css("html > body > table")
        trs = content.css("tr")
        for i in range(0, len(trs), 2):
            image_url = trs[i].css("a::attr(href)").extract_first()
            if image_url is None:
                continue
            num += 1
            captions = trs[i + 1].xpath("td/ul/li/text()").extract()
            filename = "data/%s.txt" % str(base + num)
            item = FlickrItem()
            item['captions'] = captions
            item['filename'] = filename
            item['number'] = base + num
            try:
                yield scrapy.Request(
                    image_url,
                    self.parse_image,
                    meta={"item": item})
            except scrapy.spidermiddlewares.httperror:
                print("404  %s" % image_url)

    def parse_image(self, response):
        image = response.css(".low-res-photo::attr(src)").extract_first()
        item = response.meta["item"]
        item["image"] = image
        yield item

