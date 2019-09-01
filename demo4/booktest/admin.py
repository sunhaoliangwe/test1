from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = False
    actions_on_bottom = True
    list_display = ['id', 'btitle', 'bpub_date']
    pass
# Register your models here.
# class HeroInfoAdmin(admin.ModelAdmin)
#     pass

admin.site.register(BookInfo,BookInfoAdmin)
# admin.site.register(HeroInfo,HeroInfoAdmin)