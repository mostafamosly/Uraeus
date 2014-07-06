from django.db import models
import datetime
from django.utils import timezone
from djmoney.models.fields import MoneyField
from product.models import Product
from warehouse.models import Warehouse
from core.models import Customer , Supplier

# Create your models here.
class Fulfillment_Entry(models.Model):
  so_id = models.ForeignKey('Sales_Order',to_field='id')
  deliverd = models.BooleanField(default=False)
  date_time = models.DateTimeField('date published')
  def __unicode__(self):
    return self.id
  def get_absolute_url(self):
      return reverse('fulfillment_update', kwargs={'pk': self.pk})


class Sales_Invoice(models.Model):
    so_id =models.ForeignKey('Sales_Order' , to_field='id')
    customer=models.ForeignKey('core.Customer' ,to_field='id')
    price=MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')
    date_time=models.DateTimeField('date published')
    product=models.ManyToManyField('product.Product')
    def __unicode__(self):
      return self.id
    def get_absolute_url(self):
        return reverse('Sales_Invoice_update', kwargs={'pk': self.pk})


class Sales_Order(models.Model):
    product=models.ForeignKey('product.Product', to_field='Product_Name')
    warehouse=models.ForeignKey('warehouse.Warehouse', to_field='w_name' , null=True,blank=True)
    supplier=models.ForeignKey('core.Supplier', to_field='s_name',null=True,blank=True)
    date=models.DateTimeField('date published')
    quantity= models.IntegerField(max_length=6 )
    def __unicode__(self):
      return self.id
    def get_absolute_url(self):
        return reverse('Sales_order_update', kwargs={'pk': self.pk})
