from django.contrib import admin
from .models import *


class UserMembershipInLine(admin.TabularInline):
    model = UserMembership
    extra = 0


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reporter')
    inlines = [UserMembershipInLine]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'date', 'active')
    inlines = [UserMembershipInLine]


admin.site.register(Topic)
admin.site.register(Report)
admin.site.register(Voucher)
admin.site.register(Document)
