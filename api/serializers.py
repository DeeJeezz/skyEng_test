from rest_framework import serializers

from api.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    education = serializers.CharField(source='get_education_display')
    owner = serializers.CharField(source='owner.username', write_only=True, required=False)

    class Meta:
        model = Resume
        fields = '__all__'
