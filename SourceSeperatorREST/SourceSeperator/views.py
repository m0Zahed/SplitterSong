
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from os import path
from pathlib import Path
# Create your views here.

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def UserRegistrationView(request):
    if request.method == "POST":    
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
@csrf_exempt
def UserLoginView(request):
    if request.method == "POST":
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            # A backend authenticated the credentials
            return Response({'message': 'Login successfull'}, status=status.HTTP_201_CREATED)
        return Response({'Username does not exist or Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


#

BASE_DIR = Path(__file__).resolve().parent.parent
#Media Folder path
MEDIA_ROOT = path.join(BASE_DIR, 'media')
#For serving media files
MEDIA_URL = '/media/'

@api_view(['POST'])
@csrf_exempt
def FileUploadView(request):
    file = request.FILES.get('file')
    if file:
        # Save the uploaded file to the media location
        with open(path.join(MEDIA_ROOT, file.name), 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return Response({'message': 'File uploaded successfully'},status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)