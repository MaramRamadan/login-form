# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$',views.profile , name='profile'),
	url(r'^upload/$' , views.upload_file ,name='upload_file'),
	url(r'^success/$' , views.success_upload ,name ='success_upload'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
