# from django.conf.urls import url, include
# from . import views
# from django.core.urlresolvers import reverse_lazy
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# urlpatterns = [
#     url(r'^$', password_reset,
#         {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
#     url(r'^done/$', password_reset_done, name='password_reset_done'),
#     url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
#         {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
#     url(r'^complete/$', password_reset_complete, name='password_reset_complete'),
# ]




# from django.urls import url, include
# from django.contrib.auth import views as auth_views

# from . import views


# urlpatterns = [
#     url('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     url('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     url('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     url('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
#     ]


# urlpatterns = [
    
#     path('password-reset/',
#          auth_views.PasswordResetView.as_view(
#              template_name='users/password_reset.html'
#          ),
#          name='password_reset'),

#     path('password-reset/done/',
#          auth_views.PasswordResetDoneView.as_view(
#              template_name='users/password_reset_done.html'
#          ),
#          name='password_reset_done'),

#     path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(
#              template_name='users/password_reset_confirm.html'
#          ),
#          name='password_reset_confirm'),

#     path('password-reset-complete/',
#          auth_views.PasswordResetCompleteView.as_view(
#              template_name='users/password_reset_complete.html'
#          ),
#          name='password_reset_complete'),

#     path('issues', views.all_issues, name='issues'),
# ]