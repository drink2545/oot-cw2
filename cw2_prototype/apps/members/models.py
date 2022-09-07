from django.db import models

# Create your models here.
class stock_item(models.Model):
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    cat = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()