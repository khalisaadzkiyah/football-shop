import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
        ('equipment', 'Equipment'),
        ('merch', 'Merchandise'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='jersey')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
