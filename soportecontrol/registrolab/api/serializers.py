from rest_framework import serializers
from registrolab.models import RegistroLab


class RegistroLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroLab
        fields = '__all__'