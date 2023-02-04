from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from django.shortcuts import get_object_or_404
from .models import Post
from .serializer import PostSerializer
from rest_framework.pagination import PageNumberPagination

# custom pagination class


class PostPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = 'page'


# Create your views here.

# CRUD with generic views and mixins
# a class can inherit from multiple mixins at the same times
class PostList(generics.GenericAPIView, mixins.ListModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = PostPagination

    def get(self, request):
        return self.list(request=request)


class PostCreate(generics.GenericAPIView, mixins.CreateModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def post(self, request):
        return self.create(request=request)


class PostDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'pk'  # pk is the default, but it can be changed

    def get(self, request, *args, **kwargs):
        return self.retrieve(request=request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)


class ListPostsForAuthor(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        author = self.request.user
        return Post.objects.filter(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)


'''

MANUALLY MADE CRUD WITH CLASS BASED VIEWS

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        if posts:
            # when fetching data use parameter instance
            serializer = PostSerializer(instance=posts, many=True)
            response = {
                "message": "Posts",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={'message: "No posts found"'}, status=status.HTTP_404_NOT_FOUND)


class PostCreate(APIView):
    def post(self, request):
        data = request.data
        # when sending data to validate/convert use parameter data
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            respose = {
                "message": "Post created correctly",
                "data": serializer.validated_data
            }
            return Response(data=respose, status=status.HTTP_201_CREATED)
        return Response(data={'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    def get(self, request, pk):
        data = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(instance=data)
        response = {
            "message": "Post",
            "data": serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = request.data
        serializer = PostSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={
                "message": "Post updated",
                "data": serializer.validated_data
            }, status=status.HTTP_200_OK)
        return Response(data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        response = {
            "message": "Post deleted"
        }
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)
'''
