from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .serializers import SignUpSerializer,LoginSerializer
from .tokens import create_jwt_pair_for_user

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    # authentication_classes = []
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    # authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: "OK", 400: "Invalid email or password"})
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            return Response(
                {"message": "Login successful", "tokens": tokens},
                status=status.HTTP_200_OK
            )

        return Response({"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        return Response(
            {"user": str(request.user), "auth": str(request.auth)},
            status=status.HTTP_200_OK
        )