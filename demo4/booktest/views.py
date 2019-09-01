from django.shortcuts import render
from datetime import date
from booktest.models import BookInfo, HeroInfo
from django.db.models import  F, Q, Sum, Avg
import logging
# Create your views here.

# book = BookInfo(
#     btitle='西游记',
#     bpub_date=date(1997,11,2),
#
# )
# book.save()
# HeroInfo.objects.create(
#     hname='hds',
#     hgender=0,
#     hbook_id=1
#
# )
# 模型类对象delete
# book = BookInfo.objects.get(id=6)
# res = book.delete()
# print(res)

# 模型类.objects.filter().delete()
# hero = HeroInfo.objects.filter(id=20).delete()
# print(hero)

# book = BookInfo.objects.get(btitle='射雕英雄传')
# book.btitle = '设鸟转'
# book.save()

# BookInfo.objects.filter(btitle='设鸟转').update(btitle = '射雕英雄传')

# book = BookInfo.objects.filter(id__exact=1)
# book = BookInfo.objects.filter(id=1)
# print(book)

# book = BookInfo.objects.filter(btitle__contains='湖')
# print(book)

# book = BookInfo.objects.filter(btitle__startswith='射')
# print(book)

# book = BookInfo.objects.filter(btitle__endswith='狐')
# print(book)

# book = BookInfo.objects.filter(btitle__isnull=False)
# print(book)

# book = BookInfo.objects.filter(id__in=[1, 2, 4])
# print(book)

# book = BookInfo.objects.filter(id__lt=3)
# print(book)

# book = BookInfo.objects.filter(bpub_date__year=1980)
# print(book)
# book = BookInfo.objects.filter(bpub_date__gt=date(1980, 1, 2))
# print(book)

# book = BookInfo.objects.filter(bread__gt=F('bcomment') * 3)
# logging.error(book)

# book = BookInfo.objects.filter(Q(bread=20)|Q(id__gt=4))
# logging.error(book)

# book = BookInfo.objects.filter(bread__gt=20, id__lt=3)
# logging.error(book)

# book = BookInfo.objects.exclude(id=1)
# logging.error(book)

# book = BookInfo.objects.aggregate(Sum('bread'))
# logging.error(book)

# book = BookInfo.objects.aggregate(Avg('bread'))
# logging.error(book)

# 默认是升序
# 前面加一个负号表示降序
# book = BookInfo.objects.all().order_by('-bread')
# logging.error(book)

# 一对多
# book = BookInfo.objects.get(id=1)
# heros = book.heroinfo_set.all()
# logging.error(heros)

# 多对一
# h = HeroInfo.objects.get(id=8)
# # book = h.hbook  # 书名
# book = h.hbook_id # 书的id
# logging.error(book)

# 关联过滤查询
# book = BookInfo.objects.filter(heroinfo__hname='黄蓉')
# logging.error(book)

# hero = HeroInfo.objects.filter(hbook__btitle='天龙八部')
# logging.error(hero)

# hero = HeroInfo.objects.all()[1:3] # 下标从0开始,输出序号2和3的英雄
# logging.error(hero)

# book = BookInfo.books.all()
# logging.error(book)