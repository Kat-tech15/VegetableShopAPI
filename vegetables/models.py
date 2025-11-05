from django.db import models
from django.conf import settings

class Vegetable(models.Model):
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vegetables')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price_per_kg = models.DecimalField(max_digits=8, decimal_places=2)
    available_quantity = models.DecimalField(max_digits=8, decimal_places=2, help_text='In Kilograms')
    #image = models.ImageField(upload_to='vegetable_images', null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.vendor.username}"