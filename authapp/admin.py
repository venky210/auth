from django.contrib import admin

# Register your models here.

from authapp.models import NewUser
from django.contrib.auth.admin import UserAdmin

class useradmin(UserAdmin):
    list_display=('email','username','is_staff')
    search_fields=('email','username')

admin.site.register(NewUser,useradmin)


