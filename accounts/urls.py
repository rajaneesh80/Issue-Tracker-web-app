from django.conf.urls import url, include
from . import views
from django.contrib import messages


urlpatterns = [
	url('signup', views.signup, name='signup'),
    url('login', views.login_user, name='login'),
    url('logout', views.logout_user, name='logout'),
    url('edit_profile/', views.edit_profile, name='edit_profile'),
    url('change_password', views.change_password, name='change_password'),
]


