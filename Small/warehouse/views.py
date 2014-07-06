from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import *
from django.forms import *
from warehouse.models import Warehouse , Warehouse_Section , inventory
from django.contrib.auth.decorators import login_required
# Create your views here.
class WarehouseForm(ModelForm):
    class Meta:
        model = Warehouse

@login_required
def warehouse_list(request, template_name='warehouse/warehouse_list.html'):
    products = Warehouse.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required
def warehouse_create(request, template_name='warehouse/warehouse_form.html'):
    form = WarehouseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('warehouse_list')
    return render(request, template_name, {'form':form})

@login_required
def warehouse_update(request, pk, template_name='warehouse/warehouse_form.html'):
    product = get_object_or_404(Warehouse, pk=pk)
    form = WarehouseForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('warehouse_list')
    return render(request, template_name, {'form':form})

@login_required
def warehouse_delete(request, pk, template_name='warehouse/warehouse_confirm_delete.html'):
    product = get_object_or_404(Warehouse, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('warehouse_list')
    return render(request, template_name, {'object':product})

# Create your sections here.
class SectionForm(ModelForm):
    class Meta:
        model = Warehouse_Section

@login_required
def section_list(request, template_name='warehouse/warehouse_section_list.html'):
    products = Warehouse_Section.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required
def section_create(request, template_name='warehouse/warehouse_section_form.html'):
    form = SectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('section_list')
    return render(request, template_name, {'form':form})

@login_required
def section_update(request, pk, template_name='warehouse/warehouse_section_form.html'):
    product = get_object_or_404(Warehouse_Section, pk=pk)
    form = SectionForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('section_list')
    return render(request, template_name, {'form':form})

@login_required
def section_delete(request, pk, template_name='warehouse/warehouse_section_confirm_delete.html'):
    product = get_object_or_404(Warehouse_Section, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('section_list')
    return render(request, template_name, {'object':product})


#inventpry
class inventoryForm(ModelForm):
    class Meta:
        model = inventory

@login_required

def inventory_list(request, template_name='warehouse/inventory_list.html'):
    inv = inventory.objects.all()
    for pro in inv:
      if pro.quantity<=5:
        pro.save_quantity=False
        pro.save
    data = {}
    data['object_list'] = inv
    return render(request, template_name, data)

@login_required

def inventory_create(request, template_name='warehouse/inventory_form.html'):
    form = inventoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, template_name, {'form':form})

@login_required

def inventory_update(request, pk, template_name='warehouse/inventory_form.html'):
    inv = get_object_or_404(inventory, pk=pk)
    form = inventoryForm(request.POST or None, instance=inv)
    if form.is_valid():
        form.save()
        return redirect('inventory_list')
    return render(request, template_name, {'form':form})

@login_required

def inventory_delete(request, pk, template_name='warehouse/inventory_confirm_delete.html'):
    inv = get_object_or_404(inventory, pk=pk)
    if request.method=='POST':
        inv.delete()
        return redirect('inventory_list')
    return render(request, template_name, {'object':inv})
