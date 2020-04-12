from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views as core_views
# from django.contrib.auth import logout
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    # url(r'^single_listing/(\d+)/$',views.single_listing,name='single_listing'),
    # url(r'^new/listing$',views.listing,name='listing_form'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^booking/(\d+)/$', views.booking, name='booking'),
    # url(r'^profile/(?P<username>[0-9]+)$',views.profile, name='profile'),
    # url(r'^new/image$',views.new_image,name='new_image'),
    # url(r'^listing/times(\d+)/$',views.listing_times,name='listing_times'),
    # url(r'^sign-out/$', logout, name='logout'),
   
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)