from django.conf.urls import url, include
from . import views



urlpatterns = [
	url('signup', views.signup, name='signup'),
    url('login_user', views.login_user, name='login'),
    url('logout_user', views.logout_user, name='logout'),
    url('edit_profile/', views.edit_profile, name='edit_profile'),
    url('change_password', views.change_password, name='change_password'),
]


