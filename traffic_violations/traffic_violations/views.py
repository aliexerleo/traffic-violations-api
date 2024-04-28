from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, violationSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
import jwt
from django.conf import settings

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'message': 'Invalid credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    token = jwt.encode({'user': user.username}, settings.SECRET_KEY)
    serialize = UserSerializer(instance=user)
    return Response({'token': token, 'user': serialize.data}, status=status.HTTP_200_OK)
    # # else:
    #     return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def cargar_infraccion(request):
    violation = violationSerializer(data=request.data)
    # validate token in header request
    token = request.headers.get('Authorization')
    if not token:
        return Response({'message': 'Token is required'}, status=status.HTTP_401_UNAUTHORIZED)
    if violation.is_valid():
        violation.save()
        return Response({'message': 'Violation saved'}, status=status.HTTP_201_CREATED)
    return Response({'message': 'List of persons'})