from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Register
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
    def validate(self, data):
      if data["username"] == "" and data['email'] == "":
         raise ValueError("Input fields cannot be empty")   

      check_existing_user = Register.objects.filter(email = data["email"]).first()
      if check_existing_user is not None:
         raise ValueError("Email already exist")

      else:
         return data
    def create(self, data):
           pw = data['password']
           encrypted_pwd = make_password(pw, "wedrfghgfcdxsawsedrtyuuj")
           user = Register.objects.create(
            username = data['username'],
            email = data['email'],
            phone = data['phone'],
            password = encrypted_pwd
      )
           return user
  

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials provided')

        return {
            'email': email,
            'user': user
        }
