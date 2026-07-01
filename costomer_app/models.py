from django.db import models


class costomer(models.Model):
    
    first_name = models.CharField(max_length=100)
    
    phone = models.IntegerField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    