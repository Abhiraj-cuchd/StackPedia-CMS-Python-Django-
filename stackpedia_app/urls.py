from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:slug>', views.details_page, name='details_page'),
    path('create-post', views.create_post, name='create'),
    path('update-post/<str:slug>', views.updatePost, name='update'),
    path('delete-post/<str:slug>', views.deletePost, name='delete')
    
    
] 