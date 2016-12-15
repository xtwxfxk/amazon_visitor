# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import os
import time
import logging
import random
import traceback
import datetime
import urlparse

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys

from lutils.browser import Browser

from main import BASE_DIR
from decorator import d_next_url, d_product_urls, d_find_product, try_except_response

logger = logging.getLogger('verbose')

class AmazonBase(object):

    _next_url = None
    _product_url = ''

    product_urls = []

    def __init__(self, string_proxy=None, *args, **kwargs):
        self.category = kwargs.get('category', '')
        self.keyword = kwargs.get('keyword', '')

        self.product_asin = kwargs.get('product_asin', '')
        self.product_title = kwargs.get('product_title', '')

        self.b = Browser(string_proxy=string_proxy)

        self._current_page = 1
        self._next_page_index = 1

        self.log_path = os.path.join(BASE_DIR, 'logs', datetime.date.today().isoformat())
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        self.b.load(self.home)
        self.b.down_bottom()

        self.search()

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, page_url):
        urlp = urlparse.parse_qs(page_url)
        if 'page' in urlp:
            self._current_page = int(urlp['page'][0])

    @property
    def next_page_index(self):
        return self._next_page_index

    @next_page_index.setter
    def next_page_index(self, page_url):
        urlp = urlparse.parse_qs(page_url)
        if 'page' in urlp:
            self._next_page_index = int(urlp['page'][0])

    # def next_page(self):
    #     raise NotImplementedError()
    #
    # def search(self, keyword, category=None):
    #     raise NotImplementedError()


    def _save_screenshot(self, level='info'):
        now = datetime.datetime.now()
        self.b.save_screenshot(os.path.join(self.log_path, '%s_%02d_%02d_%02d.png' % (level, now.hour, now.minute, now.second)))

    def save_screenshot_success(self):
        self._save_screenshot(level='success')
    def save_screenshot_error(self):
        self._save_screenshot(level='error')
    def save_screenshot_info(self):
        self._save_screenshot(level='info')


    def __del__(self):
        self.b.quit()


    @d_next_url(next_xpath='//a[@id="pagnNextLink"]')
    @d_product_urls()
    def search(self, *args, **kwargs):  # , keyword, category=None
        try:
            logger.info('Search: %s' % self.keyword)

            if self.category:
                logger.info('Category: %s' % self.category)
                category_ele = self.b.xpath('//option[contains(text(), "%s")]' % self.category, ignore=True)
                if category_ele is not None:
                    category_ele.click()

            # keyword_input = self.b.find_id('twotabsearchtextbox')
            # keyword_input.send_keys(self.keyword, Keys.ENTER)

            self.b.fill('field-keywords', self.keyword, Keys.ENTER) # decode('utf-8')
            self.b.sync_local()
            self.b.down_bottom()

            self.total_page = int(self.b.xpaths_local('//div[@id="pagn"]/span')[-2].text.strip())

            # next_ele = self.b.xpath('//a[@id="pagnNextLink"]')
            # slef._next_url = next_ele.get_attribute('href') if next_ele else None

        except Exception:
            self.save_screenshot_error()
            logger.error(traceback.format_exc())

    @d_next_url(next_xpath='//a[@id="pagnNextLink"]')
    @d_product_urls()
    def next_page(self, *args, **kwargs):
        if self._next_url:
            logger.info('Go Page: %s' % self.next_page_index)
            self.b.load(self._next_url)
            self.b.sync_local()
            self.b.down_bottom()
            # next_ele = self.b.xpath('//a[@id="pagnNextLink"]')
            # slef.next_url = next_ele.get_attribute('href') if next_ele else None



    @d_find_product
    def find_product(self, product_url=''): #, random_visit=False):
        # if not product_url:
        #     logger.info('Not Found Product...')
        #     return self.find_product()
        return product_url


    @try_except_response
    def random_visit(self):
        logger.info('Random Visit Product')
        if self.product_urls:
            self.b.load(random.choice(self.product_urls))
            self.b.sync_local()
            self.b.down_bottom()

    @try_except_response
    def visit_product(self):
        logger.info('Visit %s' % self._product_url)
        self.b.load(self._product_url)
        self.b.sync_local()
        self.b.down_bottom()

        self.save_screenshot_success()