from django.db import models
from category_app.models import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
            null=True,
            blank=True
          )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        upload_to='product_list/',
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name