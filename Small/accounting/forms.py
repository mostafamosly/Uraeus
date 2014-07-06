from django import forms
from django.forms import ModelForm
from accounting.models import Account
from django.views.generic.edit import FormView

class AddAccountForm(ModelForm):
    class Meta:
        model = Account
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }


class DisplayAccounts(FormView):
    model = Account
    account_list = Account.objects.all()
