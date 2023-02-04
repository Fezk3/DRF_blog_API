from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from .models import User


class SingUpSerializer(serializers.ModelSerializer):

    # to validate specific fields, they most be decribed
    email = serializers.EmailField(max_length=20)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(
        min_length=8, max_length=20, write_only=True)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password"
        ]

    # OVERRIDE create method to hash the password and assign a token
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        # create token for the user
        Token.objects.create(user=user)

        return user

    # this will validate all attrs of the obj

    def validate(self, attrs):
        email_used = User.objects.filter(email=attrs['email']).exists()

        if email_used:
            raise ValidationError("Email is used")

        return super().validate(attrs)

    '''
    this will validate specific fields -> format: validate_<field_name>
    def validate_email(self, value):
        email_used = User.objects.filter(email=value).exists

        if email_used:
            raise ValidationError("Email is used")

        return value
    '''
