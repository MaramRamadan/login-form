from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/(?P<username>[a-zA-Z0-9]+)$',views.profile , name='profile'),
	url(r'^upload/$' , views.upload_file ,name='upload_file'),
]