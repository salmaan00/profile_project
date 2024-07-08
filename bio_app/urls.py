from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('some_other_view/', some_other_view, name='some_other_view'),
    path('home/', combined_home, name='home'),  
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('profile/<str:username>/', views.view_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_portfolio/', views.edit_portfolio, name='edit_portfolio'),
    path('portfolio/<int:user_id>/', views.portfolio_view, name='portfolio'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('delete_user_profile/', views.delete_user_profile, name='delete_user_profile'),
    path('delete_portfolio/<int:portfolio_id>/', views.delete_portfolio, name='delete_portfolio'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('profile/<str:username>/projects/', user_projects_view, name='user_projects'),
    path('logout/', views.custom_logout, name='logout'),
    # path('users/', views.user_list, name='user_list'),
]
