from modelica.newsletter.models import Newsletter, Item, Section
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight')
    search_fields = ('title', 'organization', 'body')
    list_filter = ('section',)
    ordering = ('weight',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'weight')
    search_fields = ('title',)
    list_filter = ('issue',)
    ordering = ('weight',)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'month', 'year')
    search_fields = ('title',)
    list_filter = ('year',)
    ordering = ('month', 'year')

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Section, SectionAdmin)
