from django.shortcuts import render
from .models import Room, Reservation
from .serializers import RoomSerializer, ReservationSerializer
from .permissions import IsAdmin, IsUser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

   
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated, IsUser]
    
    