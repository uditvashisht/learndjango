from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    # max_length is required in CharField
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    # both fields above are required
    summary = models.TextField()
