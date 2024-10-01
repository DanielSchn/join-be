from rest_framework import serializers
from join_auth_app.models import UserProfile
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'initials', 'color']


class RegistrationSerializer(serializers.ModelSerializer):

    repeated_password = serializers.CharField(write_only=True)
    initials = serializers.CharField(required=True, write_only=True)
    color = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(write_only=True, required=True)
    last_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password', 'initials', 'color', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        initials = self.validated_data['initials']
        color = self.validated_data['color']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']

        if pw != repeated_pw:
            raise serializers.ValidationError({'error':'passwords dont match'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'user already registered with this email'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'], first_name=first_name, last_name=last_name)
        account.set_password(pw)
        account.save()

        UserProfile.objects.create(
            user=account,
            initials=initials,
            color=color,
        )

        return account