from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from django.contrib import admin
=======
>>>>>>> 92b4cd68e104861e4b4857f6cb132c1658c9a414
from wvc_app import models


# Register your models here.


<<<<<<< HEAD
from wvc_app.models import Video,Comment,Channel


admin.site.site_header="RentOrBuy"
admin.site.site_title="Admin"

@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):

    # date_hierarchy = 'created'
    search_fields = ['title', 'location',]
    list_display = ('id','title','description','datetime','path')
    # list_filter = ('status',)

# @admin.register(models.Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('pub_date','profile_photo','bio',)



@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','text','datetime')


@admin.register(models.Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_name','subscribers') 


# @admin.register(models.Timeslot)
# class TimeslotAdmin(admin.ModelAdmin):
#     list_display = ('date','start_time','end_time')



=======
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
>>>>>>> 92b4cd68e104861e4b4857f6cb132c1658c9a414
