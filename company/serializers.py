from rest_framework import serializers
from company.models import Company, CompanyPost


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CreateCompanyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPost
        fields = "__all__"


class CompanyPostSerializer(serializers.ModelSerializer):
    num_of_likes = serializers.IntegerField()
    num_of_comments = serializers.IntegerField()

    class Meta:
        model = CompanyPost
        fields = "__all__"