# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from tastypie.api import Api
from myapp.api import *

v1_api = Api(api_name='v1')


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$',views.profile , name='profile'),
	url(r'^upload/$' , views.upload_file ,name='upload_file'),
	url(r'^success/$' , views.success_upload ,name ='success_upload'),
	url(r'^api/', include(v1_api.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
