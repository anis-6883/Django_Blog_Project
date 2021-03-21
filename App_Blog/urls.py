from django.urls import path
from . import views
from .views import CreateBlog, BlogList, MyBlogs, UpdateBlog

app_name = 'App_Blog'

urlpatterns = [
    path('', BlogList.as_view(), name='blog-home'),
    path('blog_create/', CreateBlog.as_view(), name='blog-create'),
    path('my_blogs/', MyBlogs.as_view(), name='my-blogs'),
    path('blog_details/<slug:slug>/', views.blog_details, name='blog-details'),
    path('blog_edit/<int:pk>/', UpdateBlog.as_view(), name='blog-edit'),
    path('blog_delete/<int:pk>/', views.blog_delete, name='blog-delete'),
    path('comment_delete/<int:pk>/', views.comment_delete, name='comment-delete'),
    path('liked/<int:pk>/', views.liked, name='blog-liked'),
    path('unliked/<int:pk>/', views.unliked, name='blog-unliked'),
]