from django.views.generic import TemplateView, ListView
from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponse
from product.models import Product
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.
class ProductForm(ModelForm):
    class Meta:
        model = Product

@login_required
def product_list(request, template_name='product/product_list.html'):
    products = Product.objects.all()
    data = {}
    data['object_list'] = products
    return render(request, template_name, data)

@login_required
def product_create(request, template_name='product/product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

@login_required
def product_update(request, pk, template_name='product/product_form.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

@login_required
def product_delete(request, pk, template_name='product/product_confirm_delete.html'):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, template_name, {'object':product})
