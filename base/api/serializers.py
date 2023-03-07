"""
Serializes the `Room` model using Django REST Framework's `ModelSerializer`.

This serializer includes all fields of the `Room` model.

Functions:
    RoomSerializer: A class-based serializer for the `Room` model.
"""

from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):
    """
    A class-based serializer for the `Room` model.
    """
    class Meta:
        model = Room
        fields = '__all__'  # includes all fields in the model
