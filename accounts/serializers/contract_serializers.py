from rest_framework import serializers
from accounts.models.contract_info import ContactInfo


class ContractInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"

