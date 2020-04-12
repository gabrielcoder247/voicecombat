from django.contrib import admin

# Register your models here.

from wvc_app import models


# Register your models here.


from wvc_app.models import VoiceCard,Comment,TestModelWithVideoAndImage,Profile


admin.site.site_header="VoiceCombat"
admin.site.site_title="Admin"

@admin.register(models.VoiceCard)
class VoiceCardAdmin(admin.ModelAdmin):

    # date_hierarchy = 'created'
    search_fields = ['title']
    list_display = ('id','title','date','genre','video','category',)
    # list_filter = ('status',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','comment','date')


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact','address','profile_pic','video') 




    
    

    # admin.site.register(Profile)
    # admin.site.register(Image)
    # admin.site.register(Booking)
    # admin.site.register(Timeslot)
    # admin.site.register(Apartment)
    # admin.site.register(Bungalow)
