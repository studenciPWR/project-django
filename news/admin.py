from django.contrib import admin
from news.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}


#class CalendarAdmin(admin.ModelAdmin):
    #list_display = ('date')
    #prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
#admin.site.register(Calendar)