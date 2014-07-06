from django.db import models
import datetime
from django.utils import timezone
from core.models import Supplier
from product.models import Product
import moneyed
from djmoney.models.fields import MoneyField
# Create your models here.

class Procurement(models.Model):
    product=models.ForeignKey('product.Product', to_field='Product_Name')
    supplier=models.ForeignKey('core.Supplier',to_field='s_name')
    quantity=models.IntegerField(max_length=6)
    pi_id = models.ForeignKey('PurchaseInvoice' ,to_field='id' )
    recived = models.BooleanField()
    date_time = models.DateTimeField('date published')

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('procurement_update', kwargs={'pk': self.pk})


class PurchaseInvoice(models.Model):
    s_id = models.ForeignKey('core.Supplier',to_field='s_name')
    paid = models.BooleanField()
    date_time = models.DateTimeField('date published')
    price=MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')

    def __unicode__(self):
      return self.id

    def get_absolute_url(self):
        return reverse('purchaseinvoice_update', kwargs={'pk': self.pk})




class PurchaseRequision(models.Model):
  #po_id=models.ForeignKey('PurchaseOrder')
  product=models.ForeignKey('product.Product', to_field='Product_Name')
  quantity= models.IntegerField(max_length=6 )
  delivered = 'Del'
  pending = 'PEN'
  nature_choices = (
      (delivered, 'Delivered'),
      (pending, 'Pending')
  )
  status = models.CharField(max_length=2, choices=nature_choices, default=delivered)
  date_time = models.DateTimeField('date published')

  def __unicode__(self):
    return self.id
    
  def get_absolute_url(self):
      return reverse('purchaserequision_update', kwargs={'pk': self.pk})


class PurchaseOrder(models.Model):
  prq_id=models.ForeignKey('PurchaseRequision' ,to_field='id')
  s_id = models.ForeignKey('core.Supplier',related_name='supplier',to_field='s_name')
  cash='Cash'
  premiums='Prem'
  terms=(
  (cash,'cash'),
  (premiums,'Premiums')
  )
  payment_terms=models.CharField(max_length=2, choices=terms, default=cash)
  date_time = models.DateTimeField('date published')

  def __unicode__(self):
    return self.id

  def get_absolute_url(self):
      return reverse('purchaseorder_update', kwargs={'pk': self.pk})
