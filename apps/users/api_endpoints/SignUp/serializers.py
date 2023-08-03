from rest_framework import serializers
#get_user_model
from django.contrib.auth import get_user_model
User = get_user_model()
#import password validation
from django.contrib.auth.password_validation import validate_password
#import email validation
from django.core.validators import validate_email




class RegisterSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(validators=[validate_email])
    password = serializers.CharField(max_length=100, validators=[validate_password], min_length=8)

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already in use"})

        elif User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({"username": "Username is already in use"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    def update(self, instance, validated_data):
        pass
