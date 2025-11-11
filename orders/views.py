from rest_framework import generics, permissions 
from accounts.permissions import IsOwnerOrOrderOnly
from .models import Order 
from .serializers import OrderSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrOrderOnly]

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrOrderOnly]