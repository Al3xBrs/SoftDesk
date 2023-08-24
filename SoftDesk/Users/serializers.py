from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Users.models import AnyUser
from Projects.models import Contribution
from datetime import date


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = "__all__"


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
        fields = [
            "username",
            "email",
            "date_of_birth",
            "password",
            "password2",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        dob = attrs["date_of_birth"]
        today = date.today()
        if (dob.year + 15, dob.month, dob.day) > (
            today.year,
            today.month,
            today.day,
        ):
            raise serializers.ValidationError(
                "Vous devez être agé d'au moins 15 ans pour vous inscrire."
            )

        return attrs

    def create(self, validated_data):
        user = AnyUser.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            date_of_birth=validated_data["date_of_birth"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnyUser
        fields = "__all__"
