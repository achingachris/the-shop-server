from django.contrib import admin
from .models import *

# page titles
admin.site.site_header = 'Coast Woman'
admin.site.site_title = 'Coast Woman'
admin.site.index_title = 'Coast Woman Admin'

# author panel
# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('author_name',)

# category panel
# admin.site.register(Category)
@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

# magazine panel
# admin.site.register(Magazine)
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('mag_title', 'publish_date')

# article panel
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publish_date', 'author')
    prepopulated_fields = {'article_link': ('title',)}

# News panel
# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')