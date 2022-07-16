from django.contrib import admin
from django.db import models
from .models import Property


#@admin.register(Owner)

#myModels = [models.Property, models.Owner]
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    #list_display = ('id', 'name')
    pass
