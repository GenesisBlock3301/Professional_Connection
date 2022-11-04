from rest_framework import serializers
from accounts.models.Featured import Featured


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = "__all__"
