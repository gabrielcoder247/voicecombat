from django.contrib import admin

# Register your models here.

from django.contrib import admin
from wvc_app import models


# Register your models here.


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



