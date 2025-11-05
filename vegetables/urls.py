from django.urls import path
from .views import VegetableListCreateView, VegetableDetailView

urlpatterns = [
    path('', VegetableListCreateView.as_view(), name='vegetable-list'),
    path('<int:pk>/', VegetableDetailView.as_view(), name='vegetable-detail'),
]