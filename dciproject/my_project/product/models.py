from django.db import models

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=255)
    product_description = models.TextField()
    product_image_url = models.URLField()
    product_price = models.IntegerField()