from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('register/', views.register, name='blog-register'),
    path('login/', views.login_page, name='blog-login'),
    path('logout/', views.logout_page, name='blog-logout'),
    path('profile/', views.profile, name='blog-profile'),
    path('update_profile/', views.update_profile, name='blog-update-profile'),
    path('change_password/', views.change_password, name='blog-change-password')

]





