from django.contrib import admin
from .models import destinationdemo
# Register your models here.


class destinationdemoAdmin(admin.ModelAdmin):
    list_display = ('name','desc','img','price','offer')

admin.site.register(destinationdemo, destinationdemoAdmin)