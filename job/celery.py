from __future__ import absolute_import
# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import os, sys
from celery import Celery

from main import BASE_DIR

app = Celery('job', include=['job.tasks'])
# app.autodiscover_tasks(lambda: ['amazonclient.job'])

# sys.path.append(os.path.join(BASE_DIR, 'job'))
# print sys.path
# Optional configuration, see the application user guide.
app.conf.update(
    # CELERY_TASK_RESULT_EXPIRES = 3600,
    CELERY_TIMEZONE = 'Asia/Shanghai',
    BROKER_URL = 'sqla+sqlite:///%s' % os.path.join(BASE_DIR, 'tasks.db'),
    # CELERYD_HIJACK_ROOT_LOGGER = True,
    CELERYD_CONCURRENCY = 1,
    CELERYD_LOG_LEVEL = 'INFO',
    CELERY_RESULT_BACKEND = 'db+sqlite:///%s' % os.path.join(BASE_DIR, 'results.db'),
)

# if __name__ == '__main__':
#     app.start()