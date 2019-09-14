from django.urls import path, include
from .import views

urlpatterns = [

	path('issues', views.all_issues, name='issues'),

	path('my_issues', views.my_issues, name='my_issues'),
	path('edit/<int:pk>', views.edit_issue, name='edit'),

	path('new_issue', views.create_issue, name='new_issue'),
	
	path('<int:issue_id>/', views.get_detail, name='get_detail'),

	path('<int:pk>/new/', views.create_comment, name='create_comment'),
	path('<int:pk>/edit/', views.edit_comment, name='edit_comment'),

	path('<int:pk>/upvote/', views.upvote, name='upvote'),

	path('<int:pk>/delete/', views.delete_issue, name='delete_issue'),


]


