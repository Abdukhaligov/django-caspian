from django.contrib import admin
from event.admin import UserMembershipInLine
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from django.contrib.auth.models import Group, User
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    classes = ['collapse']
    extra = 1


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'get_full_name')
    list_filter = [
        'usermembership', 'profile__degree',
        'profile__rank', 'profile__public',
        'profile__reference', 'is_staff',
        'is_superuser', 'is_active', 'groups']
    search_fields = [
        'username', 'first_name',
        'last_name', 'email',
        'profile__phone', 'profile__company',
        'profile__position', 'profile__description']
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'password')
        }),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')
        }),
    )

    inlines = (ProfileInline, UserMembershipInLine)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Region)
admin.site.register(Reference)
admin.site.register(Sponsor)
