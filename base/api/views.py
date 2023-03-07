"""
Defines API views for the base app.

This module includes view functions that handle GET requests to return JSON data for the API.

Functions:
    getRoutes: Returns a list of available API routes.
    getRooms: Returns a list of all rooms in the database.
    getRoom: Returns the details of a specific room with the given id.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    """
    Returns a list of available API routes.
    """
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    """
    Returns a list of all rooms in the database.
    """
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    """
    Returns the details of a specific room with the given id.
    """
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
