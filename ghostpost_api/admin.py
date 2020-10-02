from django.contrib import admin
from . import models
# Register your models here.

class BoastRoastAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')

    
admin.site.register(models.BoastRoast, BoastRoastAdmin)