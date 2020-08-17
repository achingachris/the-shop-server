from django.contrib import admin
from .models import *

# author panel
# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('author',)

# category panel
# admin.site.register(Category)
@admin.register(Category)
class  CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

# magazine panel
# admin.site.register(Magazine)
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')

# article panel
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'publish_date', 'author')

# News panel
# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')