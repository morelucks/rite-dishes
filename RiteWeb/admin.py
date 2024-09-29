from django.contrib import admin
from RiteWeb.models import UserProfileInfo
from .models import Food, Comment, AboutUs, EPLANNING, EWEDDING, EBIRTHDAY,  ENAMING, EANNIVERSARY, EDIETING, EHOTEL, ECAFETERIA, ERENDERING, RiteGallery, Location


# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class FoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
class AboutUsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class EPLANNINGAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class EWEDDINGAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class EBIRTHDAYAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class ENAMINGAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class EANNIVERSARYAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class EDIETINGAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class EHOTELAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class ECAFETERIAAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}

class ERENDERINGAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}


class RiteGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('body',)}


admin.site.register(Location, LocationAdmin)    
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(EPLANNING, EPLANNINGAdmin)
admin.site.register(EWEDDING, EWEDDINGAdmin)
admin.site.register(EBIRTHDAY, EBIRTHDAYAdmin)
admin.site.register(ENAMING, ENAMINGAdmin)
admin.site.register(EANNIVERSARY, EANNIVERSARYAdmin)
admin.site.register(EDIETING, EDIETINGAdmin)
admin.site.register(EHOTEL, EHOTELAdmin)
admin.site.register(ECAFETERIA, ECAFETERIAAdmin)
admin.site.register(ERENDERING, ERENDERINGAdmin)
admin.site.register(RiteGallery, RiteGalleryAdmin)



