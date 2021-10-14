from rest_framework import serializers

from api.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username', write_only=True, required=False)

    class Meta:
        model = Resume
        fields = '__all__'
