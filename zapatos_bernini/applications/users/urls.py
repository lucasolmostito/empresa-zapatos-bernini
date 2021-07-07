#
from django.urls import path

from . import views

app_name = "app_users"

urlpatterns = [
    path('', views.LoginUser.as_view(), name='user-login'),
    path('users/logout/', views.LogoutView.as_view(), name='user-logout'),
]