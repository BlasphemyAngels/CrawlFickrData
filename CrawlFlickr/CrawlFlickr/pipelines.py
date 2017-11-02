# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib


class CrawlflickrPipeline(object):

    def process_item(self, item, spider):
        if item["image"] is None:
            return item
        fw_caption = open(item["filename"], "w")
        for cap in item["captions"]:
            fw_caption.write(cap + "\n")
        fw_caption.close()
        image = "https:" + item["image"]
        sup = image.rfind(".")
        sup_ = image[sup:]
        filepath = "data/%s.%s" % (str(item["number"]), sup_)
        urllib.request.urlretrieve(image, filepath)
        with open("data/match.txt", "w") as f:
            fn = "%s.txt" % str(item["number"])
            inm = "%s.%s" % (str(item["number"]), sup_)
            f.write("%s\t%s\n" % (fn, inm))
        return item
