from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponse
from accounting.models import *
from django.shortcuts import *
from django.core.context_processors import csrf
from accounting.forms import *
from django.db.models import Sum
from decimal import Decimal
import simplejson as json
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.decorators import login_required
# from reportlab.pdfgen import canvas


def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response



class Index(TemplateView):
    template_name = 'accounting/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['assets'] = Asset.objects.all()
        context['liabilities'] = Liability.objects.all()
        context['equities'] = Equity.objects.all()
        return context


# Accounts Views
class AccountForm(ModelForm):
    class Meta:
        model = Account
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def accounts_list(request, template_name='accounting/account_list.html'):
    accounts = Account.objects.all()
    data = {}
    data['object_list'] = accounts
    return render(request, template_name, data)

@login_required
def account_create(request, template_name='accounting/account_form.html'):
    form = AccountForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('account_list')
    return render(request, template_name, {'form':form})


@login_required
def account_update(request, pk, template_name='accounting/account_form.html'):
    account = get_object_or_404(Account, pk=pk)
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save()
        return redirect('account_list')
    return render(request, template_name, {'form':form})


@login_required
def account_delete(request, pk, template_name='accounting/account_confirm_delete.html'):
    account = get_object_or_404(Account, pk=pk)
    if request.method=='POST':
        account.delete()
        return redirect('account_list')
    return render(request, template_name, {'object':account})


# BalanceSheets Views
class ListBalanceSheets(ListView):
    model = BalanceSheet


class CreateBalanceSheet(CreateView):
    model = BalanceSheet
    success_url = reverse_lazy('balance_sheets_list')


# Assets Views
class AssetForm(ModelForm):
    class Meta:
        model = Asset
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def assets_list(request, template_name='accounting/asset_list.html'):
    assets = Asset.objects.all()
    data = {}
    data['object_list'] = assets
    return render(request, template_name, data)

@login_required
def asset_create(request, template_name='accounting/asset_form.html'):
    form = AssetForm(request.POST or None)
    if form.is_valid():
        form.save()
        account = Account.objects.create(name=form.data['account'],
        account_number=1001, nature='DEB',)
        account.save()
        return redirect('assets_list')
    return render(request, template_name, {'form':form})


@login_required
def asset_update(request, pk, template_name='accounting/asset_form.html'):
    asset = get_object_or_404(Asset, pk=pk)
    form = AssetForm(request.POST or None, instance=asset)
    if form.is_valid():
        form.save()
        return redirect('assets_list')
    return render(request, template_name, {'form':form})


@login_required
def asset_delete(request, pk, template_name='accounting/asset_confirm_delete.html'):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method=='POST':
        asset.delete()
        return redirect('assets_list')
    return render(request, template_name, {'object':asset})



# Liabilities Views
class LiabilityForm(ModelForm):
    class Meta:
        model = Liability
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def liabilities_list(request, template_name='accounting/liability_list.html'):
    liabilities = Liability.objects.all()
    data = {}
    data['object_list'] = liabilities
    return render(request, template_name, data)


@login_required
def liability_create(request, template_name='accounting/liability_form.html'):
    form = LiabilityForm(request.POST or None)
    if form.is_valid():
        form.save()
        account = Account.objects.create(name=form.data['account'],
        account_number=1003, nature='CRE',)
        account.save()
        return redirect('liabilities_list')
    return render(request, template_name, {'form':form})


@login_required
def liability_update(request, pk, template_name='accounting/liability_form.html'):
    liability = get_object_or_404(Liability, pk=pk)
    form = LiabilityForm(request.POST or None, instance=liability)
    if form.is_valid():
        form.save()
        return redirect('liabilities_list')
    return render(request, template_name, {'form':form})


@login_required
def liability_delete(request, pk, template_name='accounting/liability_confirm_delete.html'):
    liability = get_object_or_404(Liability, pk=pk)
    if request.method=='POST':
        liability.delete()
        return redirect('liabilities_list')
    return render(request, template_name, {'object':liability})


# Equities Views
class EquityForm(ModelForm):
    class Meta:
        model = Equity
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def equities_list(request, template_name='accounting/equity_list.html'):
    equities = Equity.objects.all()
    data = {}
    data['object_list'] = equities
    return render(request, template_name, data)


@login_required
def equity_create(request, template_name='accounting/equity_form.html'):
    form = EquityForm(request.POST or None)
    if form.is_valid():
        form.save()
        account = Account.objects.create(name=form.data['account'],
        account_number=1002, nature='CRE',)
        account.save()
        return redirect('equities_list')
    return render(request, template_name, {'form':form})


@login_required
def equity_update(request, pk, template_name='accounting/equity_form.html'):
    equity = get_object_or_404(Equity, pk=pk)
    form = EquityForm(request.POST or None, instance=equity)
    if form.is_valid():
        form.save()
        return redirect('equities_list')
    return render(request, template_name, {'form':form})


@login_required
def equity_delete(request, pk, template_name='accounting/equity_confirm_delete.html'):
    equity = get_object_or_404(Equity, pk=pk)
    if request.method=='POST':
        equity.delete()
        return redirect('equities_list')
    return render(request, template_name, {'object':equity})


def nvd3(request):
    xdata = Account.objects.values_list('name')
    ydata = []
    hamada = Account.objects.values_list('debit_balance')

    for i in hamada:
        ydata.append(json.loads(str(i[0]), use_decimal=True))

    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    print hamada
    print xdata
    print ydata
    print chartdata
    return render_to_response('accounting/piechart.html', data)
