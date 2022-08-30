from rest_framework import serializers
from api.models import Quarter

class QuarterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quarter
        fields = ('quantity')