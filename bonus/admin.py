from django.contrib import admin

from django.contrib import admin

from .models import Person, Msg

# Register your models here.
admin.site.register(Person)
admin.site.register(Msg)