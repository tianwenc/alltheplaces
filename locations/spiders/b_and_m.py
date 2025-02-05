from locations.spiders.vapestore_gb import clean_address
from locations.structured_data_spider import StructuredDataSpider

from scrapy.spiders import SitemapSpider


class BAndMSpider(SitemapSpider, StructuredDataSpider):
    name = "b_and_m"
    item_attributes = {"brand": "B&M", "brand_wikidata": "Q4836931", "country": "GB"}
    allowed_domains = ["www.bmstores.co.uk"]
    sitemap_urls = ["https://www.bmstores.co.uk/hpcstores/storessitemap"]
    sitemap_rules = [("", "parse_sd")]
    wanted_types = ["LocalBusiness"]

    def inspect_item(self, item, response):
        item["street_address"] = clean_address(item["street_address"])
        yield item
