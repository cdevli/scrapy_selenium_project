from selenium import webdriver
# chrome selenium挂代理

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://221.182.133.227:65103')
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.aifou.cn/")
print(driver.page_source)