from rest_framework import serializers
from .import models
from django.contrib.auth.models import User
from .models import UserProfile, PurchaseHistory
    
    
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username', 'first_name','last_name','email','password','confirm_password']
    
    def save(self):
        username=self.validated_data['username']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['confirm_password']
        
        if password !=password2:
            raise serializers.ValidationError({'error' : "Password didn't match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email allready exists"})
        account=User(username=username,email=email)
        account.set_password(password)
        account.is_active=False
        account.save()
        return account
    
    
class UserLoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']

class PurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseHistory
        fields = ['product_name', 'price', 'purchase_date']
        
        
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    purchase_history = PurchaseHistorySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile', 'purchase_history']
