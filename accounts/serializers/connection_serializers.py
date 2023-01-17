from rest_framework import serializers
from accounts.models.connection import Connection
from rest_framework.validators import UniqueTogetherValidator


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = "__all__"

        validators = [
            UniqueTogetherValidator(
                queryset=Connection.objects.all(),
                fields=['user1', 'user2']
            )
        ]


