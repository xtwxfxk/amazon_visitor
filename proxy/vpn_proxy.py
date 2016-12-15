# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import logging
import traceback
import urllib
logger = logging.getLogger('verbose')

class VpnProxy:
    # 代理管理器 - 控制代理使用次数
    def __init__(self, vpn_ip, vpn_port, vpn_name, vpn_username, vpn_password):

        self.ip = vpn_ip
        self.port = vpn_port

        self.name = vpn_name
        self.username = vpn_username
        self.password = vpn_password


    def get(self):
        """获取一个VPN
        """
        try:
            post_params = {
                'name': self.name,
                'username': self.username,
                'password': self.password
            }
            post_args = urllib.urlencode(post_params)
            dial_url = 'http://%s:%s/vpn-dial?%s' % (self.ip, self.port, post_args)
            logger.info('Dial Url: %s' % dial_url)

            for i in range(3):
                try:
                    current_ip = urllib.urlopen(dial_url).read().strip() # http://127.0.0.1:2070/vpn-dial?name=42.7.26.182&username=12y7&password=123
                    if current_ip:
                        logger.info('Current IP: %s' % current_ip)

                        return current_ip
                    else:
                        logger.error('Dial Error Redo!!!')
                except:
                    logger.error(traceback.format_exc())

        except Exception:
            logger.error(traceback.format_exc())

        return False