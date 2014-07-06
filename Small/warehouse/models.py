from django.db import models
from product.models import *
from core.models import *

# Create your models here.


class Warehouse(models.Model):
    w_name = models.CharField(max_length=50 , unique=True)
    w_location = models.CharField(max_length=50)
    w_capacity = models.IntegerField(max_length=50)
    def __uniciode__(self):
        return self.w_name
    def get_absolute_url(self):
        return reverse('warehouse_update', kwargs={'pk': self.pk})


class Warehouse_Section(models.Model):
    sec_name = models.CharField(max_length=50,unique=True)
    sec_capacity = models.IntegerField(max_length=50)
    products=models.ManyToManyField('product.Product',null=True,blank=True)
    warehouse_ID = models.ForeignKey('Warehouse')
    def get_absolute_url(self):
        return reverse('section_update', kwargs={'pk': self.pk})
    def __unicode__(self):
        return self.sec_name

class inventory(models.Model):
  product_name=models.ForeignKey('product.Product',to_field='Product_Name')
  quantity=models.IntegerField(max_length=50)
  supplier=models.ForeignKey('core.Supplier',to_field='s_name')
  w_house=models.ForeignKey('warehouse.Warehouse_Section',to_field='sec_name')
  save_quantity=models.BooleanField(default=True)
  def __unicode__(self):
      return self.id

  def saved(self):
    return self.quantity<=5
  saved.admin_order_field = 'quantity'
  saved.boolean = True
  saved.short_description = 'save quantity?'

  def get_absolute_url(self):
      return reverse('inventory_update', kwargs={'pk': self.pk})
