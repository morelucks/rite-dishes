from django.contrib import admin
from .models import  Continental, Fruit, Pastrils

class ContinentalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}


class FruitAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}


class PastrilsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}    

admin.site.register(Continental, ContinentalAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Pastrils, PastrilsAdmin)
