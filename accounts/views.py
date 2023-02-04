from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
from .serializer import SingUpSerializer
from .models import User

# Create your views here.


class SignUpView(GenericAPIView):
    permission_classes = []  # setting this empty will allow any user to access this view
    serializer_class = SingUpSerializer
    queryset = User.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "user created correctly",
                "data": serializer.validated_data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []
    serializer_class = SingUpSerializer
    queryset = User.objects.all()

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user:
            return Response(data={"message": "login correct", "token": user.auth_token.key}, status=status.HTTP_200_OK)

        return Response(data={"error": "login incorrect"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }
        return Response(content)
