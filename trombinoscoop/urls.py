from django.urls import path
from django.contrib import admin

from .views import login, welcome, register, add_friend, show_profile, modify_profile, ajax_check_email_field, ajax_add_friend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('login', login),
    path('welcome', welcome),
    path('ajax/checkEmailField', ajax_check_email_field),
    path('modifyProfile', modify_profile),
    path('addFriend', add_friend),
    path('showProfile', show_profile),
    path('register', register),
    path('ajax/addFriend', ajax_add_friend),

]

