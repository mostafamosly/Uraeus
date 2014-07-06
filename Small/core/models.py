from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import moneyed
from djmoney.models.fields import MoneyField
from accounting.models import Account
from product.models import Product
import datetime
from django.utils import timezone


# Create your models here.
class Module(models.Model):
    module_name = models.CharField(max_length=50)
    Enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.module_name

    def get_absolute_url(self):
        return reverse('module_update', kwargs={'pk': self.pk})


class Registration_Plan(models.Model):
    registration_plan_name = models.CharField(max_length=50)
    registration_plan_Period = models.CharField(max_length=50)
    registration_plan_Price = models.IntegerField(max_length=6)

    def __unicode__(self):
        return self.registration_plan_name

    def get_absolute_url(self):
        return reverse('registration_plan_update', kwargs={'pk': self.pk})


class Client_Plan(models.Model):
    registration_date = models.DateTimeField()
    registration_expirationDate = models.DateTimeField()
    module = models.ForeignKey('Module')
    registration_plan = models.ForeignKey('Registration_Plan')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('client_plan_update', kwargs={'pk': self.pk})


# Each item should apper on an order.
class Cart(models.Model):
    customer_ID = models.OneToOneField('Customer')
    cart_items = models.ManyToManyField('CartItem', related_name='cartItem', null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


class CartItem(models.Model):
    cart_ID = models.ForeignKey('Cart')
    product_name = models.ForeignKey('product.Product', to_field='Product_Name')
    quantity = models.IntegerField(max_length=4)

    def __unicode__(self):
        return u"%s %s" % (self.product_name, self.cart_ID)


# Basic Order.
class Order(models.Model):
    cart = models.OneToOneField('Cart')
    date_ordered = models.DateTimeField('Date Ordered')
    delivery_date = models.DateTimeField('Delivery Date')

    def __unicode__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('order_update', kwargs={'pk': self.pk})


class CustomerOrder(models.Model):
    customer_ID = models.OneToOneField('Customer')
    cart_ID = models.ForeignKey('Cart', null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)


class InvoiceItem(models.Model):
    invoice_ID = models.ForeignKey('Invoice', related_name='invoice_id')
    product_name = models.ForeignKey('product.Product', to_field='Product_Name')
    quantity = models.IntegerField(max_length=4)
    item_subtotal = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')

    def __unicode__(self):
        return u"%s %s" % (self.product_name, self.invoice_ID)

class Invoice(models.Model):
    invoiceitem = models.ManyToManyField('InvoiceItem', related_name='invoiceItem', null=True, blank=True)
    total = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')

    def __unicode__(self):
        return str(self.id)

class CustomerInvoice(models.Model):
    customer_order = models.OneToOneField('CustomerOrder')
    invoice = models.OneToOneField('Invoice')
    date_issued = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.id)


class CustomerCart(models.Model):
    customer_ID = models.OneToOneField('Customer')
    cart_ID = models.OneToOneField('Cart', null=True, blank=True)

    def __unicode__(self):
        return str(self.id)


class Supplier(models.Model):
    s_name = models.CharField(max_length=100, unique=True)
    s_email = models.EmailField(max_length=75)
    s_phone = PhoneNumberField()
    s_fax = PhoneNumberField(blank=True)
    address = models.CharField(max_length=70)
    s_account = models.ForeignKey('accounting.Account')

    def __unicode__(self):
        return self.s_name

    def get_absolute_url(self):
        return reverse('supplier_update', kwargs={'pk': self.pk})



class Customer(models.Model):
    c_user = models.OneToOneField(User, related_name="cutomer_user", null=True)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=60)
    phone = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=70)
    c_account= models.OneToOneField(
                'accounting.Account',
                related_name='customer_account',
                null=True)

    def __unicode__(self):
        return self.f_name

    def get_absolute_url(self):
        return reverse('customer_update', kwargs={'pk': self.pk})


class Report(models.Model):
    pass
