from django.contrib import admin
from .models import   DrunkDrink


class DrunkDrinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

 



admin.site.register(DrunkDrink, DrunkDrinkAdmin)