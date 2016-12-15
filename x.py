# -*- coding: utf-8 -*-
__author__ = 'xtwxfxk'

import time
from amazon.us.amazon import Amazon as Amazon_us
from amazon.jp.amazon import Amazon as Amazon_jp


# category = 'レディース' # 'すべてのカテゴリー'
# keyword = '冬コート レディース'
# title = "MIOIM セーター トップス スカート セット レディース ショート ハイネック 秋冬 保温防寒 無地 純色 スリム 長袖 カジュアル アウター インナー 2点"
# title = 'Sanrense_JP レディース コート冬 ダッフルコート おしゃれ ロングコート 防寒 カジュアル 通勤 ウールコート 毛玉ににくい(ワインレッド/ネイビー・M/Lサイズ)'
# title = '(アザブロ ガール)Azbro Girl レディース 上品 冬 あったか 純色 スナップ ボタン 長袖 着合わせ ロング コート'
# title = '(Merry & Shelly) レディース ニット ファー コート 切り替え リブ フード アウター'
# a = Amazon_jp(category=category, keyword=keyword, product_title=title) # category
#
# for i in range(20):
#     if a.find_product(random_visit=True):
#         break
#     else:
#         a.next_page()
#
# a.visit_product()
#
# print 'over'
# time.sleep(50)

###############
category = '' #''socks kid'
keyword = 'socks kid'
title = 'Naartjie Kids Girls Fashion Variety Cotton Crew 9 Pairs Gift Box'
a = Amazon_us(category=category, keyword=keyword, product_title=title) # category

for i in range(20):
    if a.find_product(random_visit=True):
        break
    else:
        a.next_page()

a.visit_product()

print 'over'
time.sleep(50)


# a.search()
#
# print a._product_url
# a.random_visit()
#
# a.next_page()
#
# a.random_visit()
#
# a.next_page()


# from lutils.browser import Browser
#
# b = Browser()
# b.load('http://www.amazon.co.jp')
# print '11111111'
# print b.xpath('//option[contains(text(), "%s")]' % 'レディース'.decode('utf-8'))
#
# time.sleep(20)


# from lutils.lrequest import LRequest
#
# lr = LRequest()
#
# lr.load('http://www.baidu.com')
# # print lr.body
# print lr.xpath(".//*[@id='u1']/a[1]").text
