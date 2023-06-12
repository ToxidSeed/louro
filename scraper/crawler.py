from scrapy.crawler import CrawlerProcess
from scraper.spiders.reverso import ContextReversoSpider
from scrapy.utils.project import get_project_settings
from config import feeds_path

def start(urls=[]):
    settings = get_project_settings()        
    #settings.set("LOG_ENABLED",False)
    #settings.set("COOKIES_ENABLED",False)
    #settings.set("DOWNLOAD_DELAY",2)    
    #settings.set("USER_AGENT",{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'})
    #settings.set("FEEDS",{"items.json": {"format": "json"}})    
    process = CrawlerProcess(settings=settings)
    process.crawl(ContextReversoSpider,start_urls=urls)
    process.start()

#LOG_ENABLED    