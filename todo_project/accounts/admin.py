from django.contrib import admin
from .models import Profile
admin.site.register(Profile)

# Register your models here.

admin.site.site_header = "Todo App Admin"
admin.site.site_title = "Todo App"
admin.site.index_title = "Dashboard Administrasi"