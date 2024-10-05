from rest_framework import serializers
from .models import Password


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)


class PasswordSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create a password
        """
        return Password.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Edit a password
        """
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.password = validated_data.get('password', instance.password)
        instance.site_url = validated_data.get('site_url', instance.site_url)
        instance.site_name = validated_data.get('site_name', instance.site_name)
        instance.notes = validated_data.get('notes', instance.notes)

        instance.save()
        return instance

    class Meta:
        model = Password
        fields = '__all__'
