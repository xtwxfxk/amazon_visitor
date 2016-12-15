# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import logging
import random
import traceback
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from ..base import AmazonBase
from ..base.decorator import d_next_url, d_product_urls, d_find_product

logger = logging.getLogger('verbose')

class Amazon(AmazonBase):

    home = 'http://www.amazon.co.jp'
    # _next_url = None
    # _product_url = ''
    #
    # product_urls = []

    def __init__(self, *args, **kwargs):
        super(Amazon, self).__init__(*args, **kwargs)

        # self.b.load(self.home)
        # self.search()


    # @d_next_url(next_xpath='//a[@id="pagnNextLink"]')
    # @d_product_urls()
    # def search(self, *args, **kwargs): # , keyword, category=None
    #     try:
    #         logger.info('Search: %s' % self.keyword)
    #
    #         if self.category:
    #             category_ele = self.b.xpath('//option[contains(text(), %s)]' % self.category, ignore=True)
    #             if category_ele is not None:
    #                 category_ele.click()
    #
    #         # keyword_input = self.b.find_id('twotabsearchtextbox')
    #         # keyword_input.send_keys(self.keyword, Keys.ENTER)
    #
    #         self.b.fill('field-keywords', self.keyword.decode('utf-8'), Keys.ENTER)
    #         self.b.sync_local()
    #         self.total_page = int(self.b.xpaths_local('//div[@id="pagn"]/span')[-2].text.strip())
    #
    #         # next_ele = self.b.xpath('//a[@id="pagnNextLink"]')
    #         # slef._next_url = next_ele.get_attribute('href') if next_ele else None
    #
    #     except Exception:
    #         self.save_screenshot()
    #         logger.error(traceback.format_exc())
    #
    #
    # @d_next_url(next_xpath='//a[@id="pagnNextLink"]')
    # @d_product_urls()
    # def next_page(self, *args, **kwargs):
    #     if self._next_url:
    #         logger.info('Next Page: %s' % self.current_page)
    #         self.b.load(self._next_url)
    #         self.b.sync_local()
    #         # next_ele = self.b.xpath('//a[@id="pagnNextLink"]')
    #         # slef.next_url = next_ele.get_attribute('href') if next_ele else None
    #
    # def random_visit(self):
    #     logger.info('Random Visit Product')
    #     if self.product_urls:
    #         self.b.load(random.choice(self.product_urls))
    #         self.b.sync_local()
    #
    # @d_find_product
    # def find_product(self, product_url='', random_visit=False):
    #     logger.info('Finding...')
    #     if not product_url:
    #         logger.info('Not Found Product...')
    #         return self.find_product()
    #
    #     return product_url
    #
    # def visit_product(self):
    #
    #     self.b.load(self._product_url)
    #     self.b.sync_local()



