from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, violationSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User
from rest_framework import status
# from django.contrib.auth import authenticate
import jwt
from django.conf import settings
from apps.report.models import Vehicle, Violation
from django.http import JsonResponse


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'message': 'Invalid credentials'},
                        status=status.HTTP_400_BAD_REQUEST)
    token = jwt.encode({'user': user.username}, settings.SECRET_KEY)
    serialize = UserSerializer(instance=user)
    return Response({'token': token, 'user': serialize.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def cargar_infraccion(request):
    violation = violationSerializer(data=request.data)
    licence_to_load = request.data['licence']
    vehicle_data = Vehicle.objects.filter(vehicle_number=licence_to_load)
    if len(vehicle_data) < 1:
        return Response({'message': 'Licence not found'}, status=status.HTTP_404_NOT_FOUND)
    token = request.headers.get('Authorization')
    if not token:
        return Response({'message': 'Token is required'}, status=status.HTTP_401_UNAUTHORIZED)
    if violation.is_valid():
        violation.save()
        return Response({'message': 'Violation added'}, status=status.HTTP_200_OK)
    return Response({'message': 'licence not match'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def generar_informe(request):
    email = request.data['email']
    violations = Violation.objects.filter(email=email)
    if len(violations) < 1:
        return Response({'message': 'No violations found'}, status=status.HTTP_404_NOT_FOUND)
    serialize = violationSerializer(instance=violations, many=True)
    return Response({'violations': serialize.data}, status=status.HTTP_200_OK)

   