from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
from django.core.urlresolvers import reverse
from core.models import *
from warehouse.models import *


# Create your models here.
class Product(models.Model):
    def upload_to(instance, filename):
        return 'product_images/%s/%s' % (instance.Product_Name, filename)

    Product_Name = models.CharField(max_length=50, unique=True)
    Barcode = models.IntegerField(max_length=13)
    Product_image = models.ImageField(upload_to=upload_to ,null=True,blank=True)
    product = 'PRO'
    service = 'SER'
    nature_choices = ((product, 'Product'),(service, 'Service'),)
    Product_Nature = models.CharField(max_length=3,choices=nature_choices,default=product)
    Product_Cost = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')
    Product_Price = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')

    def __unicode__(self):
        return self.Product_Name

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})
