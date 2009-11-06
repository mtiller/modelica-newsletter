from modelica.newsletter.models import Newsletter, Item, Section
from django.contrib import admin

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'weight')
    search_fields = ('title', 'author', 'organization', 'body')
    list_filter = ('section',)
    ordering = ('weight',)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'issue', 'weight')
    search_fields = ('title',)
    list_filter = ('issue',)
    ordering = ('weight',)

admin.site.register(Newsletter)
admin.site.register(Item, ItemAdmin)
admin.site.register(Section, SectionAdmin)
