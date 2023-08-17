from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Users.models import AnyUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        # ...

        return token


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,
    )

    class Meta:
        model = AnyUser
        fields = "__all__"

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = AnyUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            date_of_birth=validated_data["date_of_birth"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnyUser
        fields = "__all__"
