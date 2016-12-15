# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import tornado.web
import logging
import traceback
import json
import subprocess
import time
import urllib
import json

from job.tasks import visit

logger = logging.getLogger('verbose')


class VisitorHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            logger.info('Start Visit...')

            country = self.get_argument('country') # 'Japanes' 'America' # JA  US
            category = self.get_argument('category')
            keyword = self.get_argument('keyword')
            title = self.get_argument('title')
            asin = self.get_argument('asin', '')

            visit.delay(country, category, keyword, title, asin)
            self.write('')

        except:
            logger.error(traceback.format_exc())
            self.write('')
