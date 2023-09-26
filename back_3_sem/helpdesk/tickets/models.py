from django.db import models

# Create your models here.
class Ticket(models.Model):
    PRIORITIES = (
        ('low', 'низкий'),
        ('medium', 'средний'),
        ('high', 'высокий'),
    )
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    creation_date = models.DateTimeField(auto_now_add=True)
