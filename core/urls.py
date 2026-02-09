from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns=[path('',ad_list,name='ad_list'),path('ad_detail/<int:id>',ad_detail,name='ad_detail'),
             path('signup/',signup,name='signup'),path('logout/',auth_views.LogoutView.as_view(next_page='ad_list'),name='logout'),
             path('login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
             path('add_ad/',add_ad,name='add_ad'),path('my_ad',my_ad,name='my_ad'),path('edite_ad/<int:id>',edite_ad,name='edite_ad'),path('delete_ad/<int:id>',delete_ad,name='delete_ad'), path('about/',about,name='about')]