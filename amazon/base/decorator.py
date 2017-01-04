# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import logging
import functools
import time
import traceback
import urlparse

logger = logging.getLogger('verbose')

# def next_url(method):
#     def wrapper(self, *args, **kwargs):
#         method(*args, **kwargs)
#
#         next_ele = self.b.xpath('//a[@id="pagnNextLink"]')
#         self.next_url = next_ele.get_attribute('href') if next_ele else None
#
#     return wrapper

def try_except_response(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception:
            self.save_screenshot_error()
            logger.error(traceback.format_exc())
    return wrapper

def d_next_url(next_xpath='//a[@id="pagnNextLink"]'):
    def _next_url(method):
        @try_except_response
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):

            result = method(self, *args, **kwargs)

            next_ele = self.b.xpath_local(next_xpath)
            self._next_url = urlparse.urljoin(self.b.current_url, next_ele.attrib['href']) if next_ele is not None else None
            self.current_page = self.b.current_url
            self.next_page_index = self._next_url

            return result

        return wrapper
    return _next_url

def d_product_urls(product_xpath='//li[contains(@id, "result_")]//a[contains(@class, "s-access-detail-page")]', attr='href'):
    def _product_urls(method):
        @try_except_response
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)

            self.product_urls = []
            for ele in self.b.xpaths_local(product_xpath):
                if attr == 'href':
                    self.product_urls.append(urlparse.urljoin(self.b.current_url, ele.attrib[attr]))
                else:
                    self.product_urls.append(ele.attrib[attr])

            return result

        return wrapper
    return _product_urls

def d_find_product(method):
    @try_except_response
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):

        product_ele = None
        if self.product_asin:
            product_ele = self.b.xpath_local('//li[contains(@id, "result_")]//a[contains(@class, "s-access-detail-page") and contains(@href, "dp/%s")]' % self.product_asin)

        if product_ele is None:
            product_ele = self.b.xpath_local('//li[contains(@id, "result_")]//a[contains(@class, "s-access-detail-page") and contains(@title, "%s")]' % self.product_title) # .decode('utf-8')

        # if product_ele is None:
        #     if kwargs.get('random_visit', False):
        #         self.random_visit()
        #
        #     self.next_page()
        if product_ele is not None:
            self._product_url = urlparse.urljoin(self.b.current_url, product_ele.attrib['href'])
            logger.info('Found Product...')
        else:
            logger.info('Not Found Product...')

        return method(self, product_url=self._product_url, *args, **kwargs)
    return wrapper


