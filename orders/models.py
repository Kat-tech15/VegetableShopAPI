from django.db import models
from accounts.models import CustomUser
from vegetables.models import Vegetable


class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ForeignKey(Vegetable, on_delete=models.CASCADE, related_name='vegetables')
    quantity = models.IntegerField(default=1)
    ORDER_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} - {self.quantity}"

