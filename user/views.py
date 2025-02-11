from django.shortcuts import render,redirect
from rest_framework import viewsets
from .import models
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from rest_framework import status
from .models import UserProfile
from django.contrib.auth import logout
from .serializers import UserLoginSerializer, UserSerializer,LogoutSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
#for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
# Create your views here.
    
class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user)
            user.is_active = False  
            user.save()

            # Generate email confirmation token
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"https://ecom-jfvh.onrender.com/user/active/{uid}/{token}/"

            # Send email
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({"message": "Check your email for confirmation."}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')  
    else:
        return redirect('register') 
    
    
    
class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                user_data = UserSerializer(user).data
                user_data['is_superuser'] = user.is_superuser
                
                return Response({
                    "token": token.key,
                    "user": user_data,
                    "message": "Login successful"
                }, status=status.HTTP_200_OK)
            
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class UserLogoutView(APIView):
    permission_classes = [AllowAny]  # Allow logout without authentication

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            # Authenticate the user
            user = authenticate(username=username, password=password)
            if user is None:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            # Delete the token if it exists
            token = Token.objects.filter(user=user).first()
            if token:
                token.delete()
                return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is already logged out"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    

    
class UserProfileView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user