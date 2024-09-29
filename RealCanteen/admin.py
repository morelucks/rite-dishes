from django.contrib import admin
from .models import Continental2

class Continental2Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}



admin.site.register(Continental2, Continental2Admin)