## 1，selenium爬取淘宝商品信息  
   能用class定位就用class     
   selenium使用代理（不必须）  

##  2，selenium + scrapy爬取京东商品信息  
  京东的商品列表信息用pyquery解析不了  
  用scrapy里的css和xpath解析，图片的url不知道为啥只显示前4个  
  scrapy自带的css无法获取节点全部文本，xpath可以，但获取到的是list，需要join起来。  
  
  感觉selenium挺费资源的，可以的话，还是抓接口吧。
  
  
