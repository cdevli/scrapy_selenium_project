# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from urllib.parse import quote
from scrapyseleniumtest.items import ProductItem


class TaobaoSpider(Spider):
    name = 'jingdong'
    allowed_domains = ['search.jd.com']
    base_url = 'https://search.jd.com/Search?keyword='


    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + '{}&enc=utf-8&wq={}'.format(quote(keyword),quote(keyword))
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)


    # 使用xpath解析
    # image的数据只能取出前4个，不知道怎莫回事。。。。。。
    def parse(self, response):
        products = response.xpath(
            '//*[@id="J_goodsList"]/ul/li')
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath('.//div/div[3]/strong/i/text()').extract()).strip()
            item['title'] = ''.join(product.xpath('.//div/div[4]/a/em//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath('.//div/div[7]/span/a//text()').extract()).strip()
            item['image'] = ''.join(product.xpath('.//div/div[1]/a/img/@src').extract()).strip()
            item['deal'] = product.xpath('.//div/div[5]/strong/a//text()').extract_first()
            yield item

    # 使用xpath解析
    #     # image的数据只能取出前4个，不知道怎莫回事。。。。。。
    # def parse(self, response):
    #     products = response.css(
    #         '#J_goodsList > ul > li')
    #     for product in products:
    #         item = ProductItem()
    #         item['price'] = ''.join(product.css(' div > div.p-price > strong > i::text').extract()).strip()
    #         item['title'] = ''.join(product.css('div > div.p-name.p-name-type-2 > a > em::text').extract()).strip()
    #         item['shop'] = ''.join(product.css('div > div.p-shop > span > a::text').extract()).strip()
    #         item['image'] = ''.join(product.css(' div > div.p-img > a > img::attr(src)').extract()).strip()
    #         item['deal'] = product.css('div > div.p-shop > span > a::text').extract_first()
    #         # item['location'] = product.xpath('.//div[contains(@class, "location")]//text()').extract_first()
    #         yield item