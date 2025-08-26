from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for user signup and user account management (retrieve, update
    and delete).
    """

    password = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def validate(self, attrs):
        # Password required only on creation
        password = attrs.get('password', None)
        if self.instance is None and not password:
            raise serializers.ValidationError(
                {"password": "This field is required and cannot be blank."}
            )
        return attrs

    def create(self, validated_data):
        """
        Hash password when creating user.
        """
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Hash password when updating if provided.
        """
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
