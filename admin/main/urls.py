from django.contrib import admin
from django.urls import path
from .views import BlogPostViewSet, UserAPIView


urlpatterns = [
    path('blogposts', BlogPostViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path('blogposts/<str:pk>', BlogPostViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

    path('user', UserAPIView.as_view())
]

