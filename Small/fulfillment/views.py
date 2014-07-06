from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import *
from django.forms import *
from fulfillment.models import *
from warehouse.models import *
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from procurement import views



# Create your views here.
class Fulfillment_EntryForm(ModelForm):
    class Meta:
        model = Fulfillment_Entry

    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def fulfillment_entrylist(request, template_name='fulfillment/fulfillment_entry_list.html'):
    products = Fulfillment_Entry.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required
def fulfillment_entrycreate(request, template_name='fulfillment/fulfillment_entry_form.html'):
    form = Fulfillment_EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fulfillment_list')
    return render(request, template_name, {'form':form})

@login_required
def fulfillment_entryupdate(request, pk, template_name='fulfillment/fulfillment_entry_form.html'):
    product = get_object_or_404(Fulfillment_Entry, pk=pk)
    form = Fulfillment_EntryForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('fulfillment_list')
    return render(request, template_name, {'form':form})

@login_required
def fulfillment_entrydelete(request, pk, template_name='fulfillment/fulfillment_entry_confirm_delete.html'):
    product = get_object_or_404(Fulfillment_Entry, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('fulfillment_list')
    return render(request, template_name, {'object':product})



# Create your views here.
class Sales_InvoiceForm(ModelForm):
    class Meta:
        model = Sales_Invoice

@login_required
def Sales_Invoicelist(request, template_name='fulfillment/sales_invoice_list.html'):
    products = Sales_Invoice.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required
def Sales_Invoicecreate(request, template_name='fulfillment/sales_invoice_form.html'):
    form = Sales_Invoice_EntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Sales_Invoice_list')
    return render(request, template_name, {'form':form})

@login_required
def Sales_Invoiceupdate(request, pk, template_name='fulfillment/sales_invoice_form.html'):
    product = get_object_or_404(Sales_Invoice, pk=pk)
    form = Sales_InvoiceForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('Sales_Invoice_list')
    return render(request, template_name, {'form':form})

@login_required
def Sales_Invoicedelete(request, pk, template_name='fulfillment/sales_invoice_confirm_delete.html'):
    product = get_object_or_404(Sales_Invoice, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('Sales_Invoice_list')
    return render(request, template_name, {'object':product})


# Create your views here.
class Sales_OrderForm(ModelForm):
    class Meta:
        model = Sales_Order

@login_required
def Sales_Orderlist(request, template_name='fulfillment/sales_order_list.html'):
    products = Sales_Order.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required

def Sales_Ordercreate(request,template_name='fulfillment/sales_order_form.html'):
    form = Sales_OrderForm(request.POST or None)
    if form.is_valid():
        p=inventory.objects.get(product_name = form.data['product'])
        if p.quantity >= int(form.data['quantity']):
          p.quantity -= int(form.data['quantity'])
          p.save()
          form.save()
          return redirect('Sales_order_list')
        elif p.quantity < int(form.data['quantity']):
          return redirect('purchaserequision_create')   
    return render(request, template_name, {'form':form})

@login_required
def Sales_Orderupdate(request, pk, template_name='fulfillment/sales_order_form.html'):
    product = get_object_or_404(Sales_Order, pk=pk)
    form = Sales_OrderForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('Sales_order_list')
    return render(request, template_name, {'form':form})

@login_required
def Sales_Orderdelete(request, pk, template_name='fulfillment/Sales_order_confirm_delete.html'):
    product = get_object_or_404(Sales_Order, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('Sales_order_list')
    return render(request, template_name, {'object':product})
