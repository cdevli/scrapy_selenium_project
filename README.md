## 1，selenium爬取淘宝商品信息  
   能用class定位就用class     
   selenium使用代理（不必须）  

##  2，selenium + scrapy爬取京东商品信息  
  京东的商品列表信息用pyquery解析不了  
  用scrapy里的css和xpath解析，图片的url不知道为啥只显示前4个  
  scrapy自带的css无法获取节点全部文本，xpath可以，但获取到的是list，需要join起来。  
  
  感觉selenium挺费资源的，可以的话，还是抓接口吧。
  
  
## 3，使用CrawlSpider类爬取京东商品详情和价格（jd_crawl_spider）  
主要是先获取所有请求，从中提取京东的商品详情页  
从详情页获取商品id  https://item.jd.com/7012222.html  
请求两个接口  
https://item.m.jd.com/ware/detail.json?wareId=7012222  
https://p.3.cn/prices/mgets?type=1&skuIds=J_7012222  
保存到mongodb数据库


## 4，Scrapy框架的使用之Scrapy爬取新浪微博  
https://juejin.im/post/5b052d526fb9a07ac5608078  
我们从几个大V开始抓取，抓取他们的粉丝、关注列表、微博信息，然后递归抓取他们的粉丝和关注列表的粉丝、关注列表、微博信息，递归抓取，最后保存微博用户的基本信息、关注和粉丝列表、发布的微博。  



