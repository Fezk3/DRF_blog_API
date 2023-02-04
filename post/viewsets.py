'''
******* Normally this would go on the views file ********
'''

from rest_framework import viewsets, status
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


'''
when using modelviewset/viewset, its necessary to use a router on the urls.py
the router will map the requests to the viewset automatically
'''

# CRUD with ModelViewSet


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''

    CRUD with viewset

    Manually made funtions, since its when the class inhered from viewset

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        post = request.data
        serializer = PostSerializer(data=post)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, resquest, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=post, data=resquest.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
