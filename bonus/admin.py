from django.contrib import admin

from django.contrib import admin

from .models import User, Msg

# Register your models here.
admin.site.register(User)
admin.site.register(Msg)