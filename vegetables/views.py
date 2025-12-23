from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Vegetable
from .serializers import VegetableSerializer

class VegetableListCreateView(generics.ListCreateAPIView):
    serializer_class = VegetableSerializer
    queryset = Vegetable.objects.all().order_by('-date_posted')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Yuo must be logged in to post a vegetable.")
        serializer.save(vendor=self.request.user)

    

class VegetableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': f"Vegetable '{instance.name}' has been deleted successfully"}, status=status.HTTP_200_OK)
