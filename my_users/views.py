from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from my_users.models import User
from my_users.serializers import UserSerializer


class UserView(APIView):

    def get(self, request, format=None):
        """
        Get list of users
        :param request:
        :return:
        """
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        Create new user
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, format=None):
        """
        Update user
        :param request:
        :param user_id:
        :return:
        """
        pass

    def delete(self, request, user_id, format=None):
        """
        Delete user
        :param request:
        :param user_id:
        :return:
        """
        pass