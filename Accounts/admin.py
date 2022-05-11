from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Avatar

admin.site.register(User, UserAdmin)
admin.site.register(Avatar)

# Register your models here.
