from django.contrib import admin
from .models import *


class DegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserMembershipInLine(admin.TabularInline):
    model = UserMembership
    extra = 0


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [UserMembershipInLine]


admin.site.register(Region)
admin.site.register(Reference)
admin.site.register(Degree)
admin.site.register(Membership)
admin.site.register(User, UserAdmin)
admin.site.register(Event)
admin.site.register(Topic)
admin.site.register(UserMembership)
