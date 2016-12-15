#from __future__ import absolute_import
# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import logging
from celery import app
# from celery import task

from _main import BASE_DIR

logger = logging.getLogger('verbose')


@app.task #(name='amazonclient.job.tasks.sync_order')
def visit(*args, **kwargs):
    from services import visit as _visit
    _visit(*args, **kwargs)

