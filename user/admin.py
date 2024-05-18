from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

from .models import User


class Admin(UserAdmin):
    list_display = ('phone', 'username', 'is_active', 'pk',)
    filter_horizontal = ()
    list_filter = ('is_active',
                   ('joined_at', JDateFieldListFilter))
    fieldsets = ()
    search_fields = ('username', 'phone')
    list_display_links = ('phone', 'username')


admin.site.register(User, Admin)
