# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import os
import logging
import logging.config
import ConfigParser
import traceback
import tornado.ioloop
import tornado.web
from celery import Celery

from main import BASE_DIR

from proxy import VpnProxy

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging.conf'))
logger = logging.getLogger('verbose')

# app = Celery('amazon_visitor')

def read_settings():
    """Read settings
    """
    cfg = ConfigParser.ConfigParser()
    cfg.read('settings.ini')
    settings = {}

    # 最大翻页数
    try:
        settings['max_page'] = int(cfg.get('setting', 'max_page'))
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['max_page'] = 20

    # IP每日最大使用次数
    try:
        settings['ip_max_used_times'] = int(cfg.get('setting', 'ip_max_used_times'))
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['ip_max_used_times'] = 10

    # 页面访问间隔（秒）
    try:
        settings['page_access_interval'] = float(cfg.get('setting', 'page_access_interval'))
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['page_access_interval'] = 2

    # 是否隐藏浏览器窗口（0-否，1-是）
    try:
        settings['hide_browser_window'] = cfg.get('setting', 'hide_browser_window').strip() == '1'
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['hide_browser_window'] = False

    # 选择下拉框次数
    try:
        settings['manipulate_select_box_times'] = int(cfg.get('setting', 'manipulate_select_box_times'))
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['manipulate_select_box_times'] = 1

    # 页面访问间隔（秒）
    try:
        settings['manipulate_select_box_interval'] = float(
            cfg.get('setting', 'manipulate_select_box_interval'))
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['manipulate_select_box_interval'] = 3

    # vpn 配置
    try:
        settings['vpn_ip'] = cfg.get('setting', 'vpn_ip')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['vpn_ip'] = ''
    try:
        settings['vpn_port'] = cfg.get('setting', 'vpn_port')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['vpn_port'] = ''
    try:
        settings['vpn_name'] = cfg.get('setting', 'vpn_name')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['vpn_name'] = ''
    try:
        settings['vpn_username'] = cfg.get('setting', 'vpn_username')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['vpn_username'] = ''
    try:
        settings['vpn_password'] = cfg.get('setting', 'vpn_password')
    except (ConfigParser.NoSectionError, ConfigParser.NoOptionError), e:
        settings['vpn_password'] = ''

    return settings

project_settings = read_settings()
vpn_proxy = VpnProxy(project_settings['vpn_ip'], project_settings['vpn_port'], project_settings['vpn_name'], project_settings['vpn_username'], project_settings['vpn_password'])

def make_app():
    from handler.amazon_handler import VisitorHandler

    return tornado.web.Application([
        (r"/visit", VisitorHandler),
    ])


def init_server(ip, port):
    app = make_app()
    app.listen(port=port, address=ip)
    tornado.ioloop.IOLoop.current().start()


def init_task():
    from celery.bin import worker
    from job.celery import app

    worker = worker.worker(app=app)

    options = {
        # 'loglevel': 'INFO',
        # 'traceback': True,
        'CONCURRENCY': 1
    }
    worker.run() #**options)