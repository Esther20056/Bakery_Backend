from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, loginSerializer


@api_view(['post'])
def Signup(request):
   try:
     new_user_serializer = UserSerializer(data=request.data)

     if new_user_serializer.is_valid():
      new_user_serializer.save()
      return Response(new_user_serializer.data, status=status.HTTP_201_CREATED)
     else:
      return Response({"error" :"Input fields can't be empty"}, status=status.HTTP_400_BAD_REQUEST)   
   except BaseException as e: 
      return Response(str(e))
   
@api_view(['POST'])
def Login(request):
   try:
      user = loginSerializer(data=request.data)

      if user.is_valid():
         checkuser = user.loginuser(user.data)
         
         return Response(checkuser, status=status.HTTP_200_OK)
      else:
         return Response(user.errors, status=status.HTTP_400_BAD_REQUEST) 
   except BaseException as a :
     return Response(str(a), status=status.HTTP_400_BAD_REQUEST)
   
