from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('updateProfile/<str:pk>', views.UpdateProfile, name='Update_Profile'),
    path('deleteProfile', views.DeleteProfile, name='Delete_Profile'),
    path('register-user', views.registerUser, name='register_user'),
    path('login-user', views.loginUser, name='login_user'),
    path('logout-user', views.logoutUser, name='logout_user'),
]
