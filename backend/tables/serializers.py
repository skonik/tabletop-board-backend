from rest_framework import serializers

from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = [
            'title',
            'header_image',
            'description',
            'owner',
            'game',
            'start_date',
        ]
