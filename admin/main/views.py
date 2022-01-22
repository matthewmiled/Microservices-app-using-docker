from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost, User
from .serializers import BlogPostSerializer
from .producer import publish
import random

class BlogPostViewSet(viewsets.ViewSet):
    def list(self, request):               # api endpoint of: GET /api/blogposts
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)

        return Response(serializer.data)

    def create(self, request):             # api endpoint of: POST /api/blogposts
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        publish('blogpost_created', serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):  # api endpoint of: GET /api/blogposts/<str:id>
        
        try:
            blog_post = BlogPost.objects.get(id=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BlogPostSerializer(blog_post)

        return Response(serializer.data)

    def update(self, request, pk=None):    # api endpoint of: POST /api/blogposts/<str:id>
        try:
            blog_post = BlogPost.objects.get(id=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BlogPostSerializer(instance=blog_post, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        publish('blogpost_updated', serializer.data)

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):    # api endpoint of: DELETE /api/blogposts/<str:id>
        try:
            blog_post = BlogPost.objects.get(id=pk)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        blog_post.delete()

        publish('blogpost_deleted', pk)

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        
        # Returns a random user id from all of the ids defined in the User model/table
        return Response({
            'id': user.id
        })