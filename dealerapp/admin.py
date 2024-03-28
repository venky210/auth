from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from dealerapp.models import Dealer
from django.contrib.auth.admin import UserAdmin

class useradmin(UserAdmin):
    list_display=('email','username','is_staff')
    search_fields=('email','username')

admin.site.register(Dealer,useradmin)


