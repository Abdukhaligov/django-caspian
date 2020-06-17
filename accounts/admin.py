from django.contrib import admin
from events.admin import UserMembershipInLine
from .models import *
from django.utils.translation import ugettext_lazy as _


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'degree', 'email', 'phone', 'company', 'position', 'rank')
    fieldsets = (
        (None, {
            'fields': ('degree', 'name', 'email', 'phone', 'avatar_tag')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('avatar', 'company', 'position', 'rank'),
        }),
    )
    readonly_fields = ('avatar_tag',)
    inlines = [UserMembershipInLine]
    list_filter = ['usermembership', 'degree', 'rank', 'public', 'reference', ]
    search_fields = ['name', 'email', 'phone', 'company', 'position', 'description']


admin.site.register(Region)
admin.site.register(Reference)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Sponsor)
