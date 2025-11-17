from rest_framework import generics
from rest_framework import permissions
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Vegetable
from .serializers import VegetableSerializer

class VegetableListCreateView(generics.ListCreateAPIView):
    
    queryset = Vegetable.objects.all().order_by('-date_posted')
    serializer_class = VegetableSerializer

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated]
        return [permissions.AllowAny()]

class VegetableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer

    def get_permissions(self):
        if self.request.methid in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]