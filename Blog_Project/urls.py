from django.contrib import admin
from django.urls import path, include

# For Media
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Blog.urls')),
    path('', include('App_Login.urls')),

    path('password_reset/', 
    auth_views.PasswordResetView.as_view(template_name='App_Login/password_reset.html'), 
    name='password_reset'),

    path('password_reset/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name='App_Login/password_reset_done.html'), 
    name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='App_Login/password_reset_confirm.html'), 
    name='password_reset_confirm'),

    path('password_reset_complete/', 
    auth_views.PasswordResetCompleteView.as_view(template_name='App_Login/password_reset_complete.html'), 
    name='password_reset_complete')
]

# For Media
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)