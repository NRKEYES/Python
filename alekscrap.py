import scrapy
print "does this work"


class ALEKSspider(CrawlSpider):
	name = 'test'
	allowed_domains = 'aleks.com'
	start_urls = 'http://www.aleks.com'

