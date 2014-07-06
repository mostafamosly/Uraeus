from django.db import models
import moneyed
from djmoney.models.fields import MoneyField


# Create your models here.
class BalanceSheet(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    balanced = models.BooleanField(default=True)


class Asset(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    account= models.OneToOneField('Account')
    balance_sheet= models.ForeignKey('BalanceSheet')

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


class Liability(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    account= models.OneToOneField('Account')
    balance_sheet= models.ForeignKey('BalanceSheet')

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


class Equity(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, unique=True)
    account= models.OneToOneField('Account')
    balance_sheet= models.ForeignKey('BalanceSheet')

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})


class Account(models.Model):
    def __unicode__(self):
        return self.name

    debit = 'DEB'
    credit = 'CRE'
    name = models.CharField(max_length=50, unique=True)
    account_number = models.IntegerField()
    debit_balance = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')
    credit_balance = MoneyField(max_digits=10, decimal_places=2, default_currency='EGP')
    nature_choices = ((debit, 'Debit'),(credit, 'Credit'),)
    nature = models.CharField(max_length=3, choices=nature_choices, default=debit)
    date_added = models.DateTimeField(auto_now_add=True)


class IncomeStatement(models.Model):
    pass


class GeneralLedger(models.Model):
    pass
