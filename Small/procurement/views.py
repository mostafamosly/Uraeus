from django.views.generic import TemplateView, ListView
from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponse
from django.forms import ModelForm
from procurement.models import *
from django.contrib.auth.decorators import login_required
from warehouse.models import *
# Create your views here.
class ProcurementForm(ModelForm):
    class Meta:
        model = Procurement

@login_required
def Procurement_list(request, template_name='procurement/pro_list.html'):
    pros = Procurement.objects.all()
    data = {}
    data['object_list'] = pros
    return render(request, template_name, data)

@login_required
def Procurement_create(request, template_name='procurement/pro_form.html'):
    form = ProcurementForm(request.POST or None)
    if form.is_valid():
        p=inventory.objects.get(product_name = form.data['product'])
        p.quantity += int(form.data['quantity'])
        p.save()
        form.save()
        return redirect('procurement_list')
    return render(request, template_name, {'form':form})

@login_required
def Procurement_update(request, pk, template_name='procurement/pro_form.html'):
    pro = get_object_or_404(Procurement, pk=pk)
    form = ProcurementForm(request.POST or None, instance=pro)
    if form.is_valid():
        form.save()
        return redirect('procurement_list')
    return render(request, template_name, {'form':form})

@login_required
def Procurement_delete(request, pk, template_name='procurement/pro_confirm_delete.html'):
    pro = get_object_or_404(Procurement, pk=pk)
    if request.method=='POST':
        pro.delete()
        return redirect('procurement_list')
    return render(request, template_name, {'object':pro})


class ListInvoice(ListView):
    model = PurchaseInvoice
    #success_url = reverse_lazy('list_invoice')

class PurchaseInvoiceForm(ModelForm):
    class Meta:
        model = PurchaseInvoice


def PurchaseInvoice_list(request, template_name='procurement/purchaseinvoice_list.html'):
    pis = PurchaseInvoice.objects.all()
    data = {}
    data['object_list'] = pis
    return render(request, template_name, data)

def PurchaseInvoice_create(request, template_name='procurement/purchaseinvoice_form.html'):
    form = PurchaseInvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('purchaseinvoice_list')
    return render(request, template_name, {'form':form})

def PurchaseInvoice_update(request, pk, template_name='procurement/purchaseinvoice_form.html'):
    pi = get_object_or_404(PurchaseInvoice, pk=pk)
    form = PurchaseInvoiceForm(request.POST or None, instance=pi)
    if form.is_valid():
        form.save()
        return redirect('purchaseinvoice_list')
    return render(request, template_name, {'form':form})

def PurchaseInvoice_delete(request, pk, template_name='procurement/purchaseinvoice_confirm_delete.html'):
    pi = get_object_or_404(PurchaseInvoice, pk=pk)
    if request.method=='POST':
        pi.delete()
        return redirect('purchaseinvoice_list')
    return render(request, template_name, {'object':pi})

# Requisition Views
class PurchaseRequisionForm(ModelForm):
    class Meta:
        model = PurchaseRequision

def purchaserequision_list(request, template_name='procurement/purchaserequision_list.html'):
    prs = PurchaseRequision.objects.all()
    data = {}
    data['object_list'] = prs
    return render(request, template_name, data)

def purchaserequision_create(request, template_name='procurement/purchaserequision_form.html'):
    form = PurchaseRequisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('purchaserequision_list')
    return render(request, template_name, {'form':form})

def purchaserequision_update(request, pk, template_name='procurement/purchaserequision_form.html'):
    pr = get_object_or_404(PurchaseRequision, pk=pk)
    form = PurchaseInvoiceForm(request.POST or None, instance=pr)
    if form.is_valid():
        form.save()
        return redirect('purchaserequision_list')
    return render(request, template_name, {'form':form})


def purchaserequision_delete(request, pk, template_name='procurement/purchaserequision_confirm_delete.html'):
    pr = get_object_or_404(PurchaseRequision, pk=pk)
    if request.method=='POST':
        pr.delete()
        return redirect('purchaserequision_list')
    return render(request, template_name, {'object':pr})


# Order Views
class PurchaseOrderForm(ModelForm):
    class Meta:
        model = PurchaseOrder

def PurchaseOrder_list(request, template_name='procurement/purchaseorder_list.html'):
    pis = PurchaseOrder.objects.all()
    data = {}
    data['object_list'] = pis
    return render(request, template_name, data)

def PurchaseOrder_create(request, template_name='procurement/purchaseorder_form.html'):
    form = PurchaseOrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('purchaseorder_list')
    return render(request, template_name, {'form':form})

def PurchaseOrder_update(request, pk, template_name='procurement/purchaseorder_form.html'):
    pi = get_object_or_404(PurchaseOrder, pk=pk)
    form = PurchaseOrderForm(request.POST or None, instance=pi)
    if form.is_valid():
        form.save()
        return redirect('purchaseorder_list')
    return render(request, template_name, {'form':form})

def PurchaseOrder_delete(request, pk, template_name='procurement/purchaseorder_confirm_delete.html'):
    pi = get_object_or_404(PurchaseOrder, pk=pk)
    if request.method=='POST':
        pi.delete()
        return redirect('purchaseorder_list')
    return render(request, template_name, {'object':pi})
