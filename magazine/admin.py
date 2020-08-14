from django.contrib import admin
from .models import Magazine, Issue, Category, Article

# admin.site.register(Magazine)
@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ('magazine_id', 'mag_issue', 'mag_date1', 'mag_date2')
    list_filter = ('mag_issue',)



admin.site.register(Issue)
admin.site.register(Category)
admin.site.register(Article)