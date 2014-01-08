from django.contrib import admin
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'category', 'url']}),
        ('View information', {'fields': ['views']}),
    ]
    list_display = ('title', 'category', 'url')
    list_filter = ['views']

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
