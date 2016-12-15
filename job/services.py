# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import logging
import traceback
from amazon.us.amazon import Amazon as Amazon_us
from amazon.jp.amazon import Amazon as Amazon_ja

from _main import  BASE_DIR

logger = logging.getLogger('verbose')


# 'Japanes' 'America' # JA  US
def visit(country, category, keyword, title, asin='', **kwargs):
    try:
        from _main import vpn_proxy
        from _main import project_settings

        ip = vpn_proxy.get()
        if not ip:
            logger.error('VPN Error')
            return
        else:
            logger.info('USE VPN: %s' % ip)

        if country == 'JA':
            a = Amazon_ja(category=category, keyword=keyword, product_title=title, product_asin=asin)  # category
        elif country == 'US':
            a = Amazon_us(category=category, keyword=keyword, product_title=title, product_asin=asin)  # category

        while a.current_page < project_settings['max_page'] and a.current_page < a.total_page:
            if a.find_product():  # random_visit=True):
                a.visit_product()
                break
            else:
                if a.current_page == 1:
                    a.random_visit()
                a.next_page()
    except:
        logger.error(traceback.format_exc())


