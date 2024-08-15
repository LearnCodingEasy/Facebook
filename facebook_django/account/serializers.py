# Page [ account/serializers.py ]

from rest_framework import serializers

from .models import User, FriendshipRequest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "personal_phone",
            "public_phone",
            "address",
            "gender",
            "workplace_company",
            "workplace_position",
            "workplace_city_town",
            "workplace_description",
            "workplace_time_period",
            "date_of_birth",
            "get_avatar",
            "get_cover",
            "friends_count",
            "posts_count",
        )


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        fields = (
            "id",
            "created_by",
        )
