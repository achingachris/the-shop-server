from django.contrib import admin
from .models import Magazine, Issue, Category, Article


# Custom Admin Page
admin.site.site_header = "The Coast Woman Admin"
admin.site.site_title = "Coast Woman"
admin.site.index_title = "Coast Woman Admin"

# Models Admin
# admin.site.register(Magazine)
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('magazine_id', 'mag_issue', 'mag_date1', 'mag_date2')
    list_filter = ('mag_issue',)

# admin.site.register(Issue)
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'issue_pub_date', 'issue_status')
    list_filter = ('issue_id', 'issue_status',)

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'article_status', 'category', 'article_issue')
    list_filter = ('author', 'article_status', 'category', 'article_issue')