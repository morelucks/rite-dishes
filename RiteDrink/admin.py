from django.contrib import admin
from .models import Drink

class DrinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}



admin.site.register(Drink, DrinkAdmin)