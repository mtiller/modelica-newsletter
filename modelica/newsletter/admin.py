from modelica.newsletter.models import Newsletter, Item, Section
from django.contrib import admin
from django.contrib.auth.models import User, Group

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'weight')
    search_fields = ('title', 'organization', 'body')
    list_filter = ('section','author')
    ordering = ('weight',)
    # Override who is allowed to change things
    def has_change_permission(self, request, obj=None):
        # If we aren't concerned with a particular item, say yes
        if not obj:
            return True # So they can see the change list
        # If the person is the author, they can change it
        if request.user==obj.author:
            return True
        # Find the editor group
        editors = Group.objects.filter(name='Editors')[0]
        # If the current user is an editor then they can change it
        if editors in request.user.groups.all():
            return True
        # If they are a super user they can change it
        if request.user.is_superuser:
            return True
        # Otherwise, no change allowed
        return False

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
