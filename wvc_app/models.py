from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt

from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video




class Profile(models.Model):

    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=70,blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    video = models.ForeignKey('TestModelWithVideoAndImage',null=True, on_delete=models.CASCADE, related_name='profile_video')
    voice = models.ForeignKey('VoiceCard',null=True, on_delete=models.CASCADE, related_name='profile_voices')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user_booking')
    profile_pic = models.ImageField(upload_to = 'images/')
    # listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='listing_booking')
    # Timeslot = models.ForeignKey('Timeslot', on_delete=models.CASCADE, related_name='timeslot_booking')
   
    

    @classmethod  
    def search_profiles(cls,name):
        profile = Profile.objects.filter_by_name(name__icontains=name).all()

        return profile


    # @classmethod   
    # def get_all_booking(cls,id):
    #     booking=Booking.objects.filter(id=id).all()

    def save_user(self):
         self.save()

    def delete_profiles(self):
        self.delete()     

    def __str__(self):
        return self.name



class TestModelWithVideoAndImage(models.Model):
    name = models.CharField(max_length=100)
    video = models.ImageField(upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                              validators=[validate_video])
    image = models.ImageField(upload_to='images/', blank=True)  # no need to set storage, field will use the default one        





class VoiceCard(models.Model):


    rap = "rap"
    dancehall = "dancehall"
    gospel = "gospel"

    PROPERTY_CHOICES = [
    (rap, "rap"),
    (dancehall, "dancehall"),
    (gospel, "gospel")
    ]

    title = models.CharField(max_length=50,)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    genre = models.EmailField(max_length=70,blank=True, null=True)
    video = models.ForeignKey(TestModelWithVideoAndImage,null=True, on_delete=models.CASCADE, related_name='voices')
    category = models.CharField(max_length=255,null=True, choices=PROPERTY_CHOICES, default=rap)
   
    class meta:
        ordering = ['-date'] 


    @classmethod
    def search_voice_card(cls, search_term):
        voice_cards = cls.objects.filter(title__icontains=search_term)
        return  voice_cards
                       


    def save_voice_card(self):
        self.save()

    @classmethod
    def get_all_voice_card(cls,id):
        voice_card = cls.objects.filter(id=id).order_by('-date')
        return voice_card

    def __str__(self):
        return str(self.date)





class Comment(models.Model):
   

    comment = models.CharField(max_length=500,null=True)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    

    @classmethod
    def get_all(cls):
        comment = cls.objects.all()
        return comment


    def save_comment(self):
        self.save()  

    def delete_comment(self):
        self.delete()      


    def __str__(self):
        return self.comment
