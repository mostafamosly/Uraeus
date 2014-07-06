from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.http import HttpResponse
from core.models import *
from django.shortcuts import *
from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.decorators import login_required
from product.models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import simplejson as json
from django import forms


#module views
class ModuleForm(ModelForm):
    class Meta:
        model = Module
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))



@login_required
def module_list(request, template_name='core/module_list.html'):
    modules = Module.objects.all()
    data = {}
    data['object_list'] = modules
    return render(request, template_name, data)


@login_required
def module_create(request, template_name='core/module_form.html'):
    form = ModuleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('module_list')
    return render(request, template_name, {'form':form})


@login_required
def module_update(request, pk, template_name='core/module_form.html'):
    module = get_object_or_404(Module, pk=pk)
    form = ModuleForm(request.POST or None, instance=module)
    if form.is_valid():
        form.save()
        return redirect('module_list')
    return render(request, template_name, {'form':form})


@login_required
def module_delete(request, pk, template_name='core/module_confirm_delete.html'):
    module = get_object_or_404(Module, pk=pk)
    if request.method=='POST':
        module.delete()
        return redirect('module_list')
    return render(request, template_name, {'object':module})


#Registration_Plan views
class Registration_PlanForm(ModelForm):
    class Meta:
        model = Registration_Plan
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def registration_plan_list(request, template_name='core/registration_plan_list.html'):
    plans = Registration_Plan.objects.all()
    data = {}
    data['object_list'] = plans
    return render(request, template_name, data)


@login_required
def registration_plan_create(request, template_name='core/registration_plan_form.html'):
    form = Registration_PlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registration_plan_list')
    return render(request, template_name, {'form':form})


@login_required
def registration_plan_update(request, pk, template_name='core/registration_plan_form.html'):
    plan = get_object_or_404(Registration_Plan, pk=pk)
    form =Registration_PlanForm(request.POST or None, instance=plan)
    if form.is_valid():
        form.save()
        return redirect('registration_plan_list')
    return render(request, template_name, {'form':form})


@login_required
def registration_plan_delete(request, pk, template_name='core/registration_plan_confirm_delete.html'):
    plan = get_object_or_404(Registration_Plan, pk=pk)
    if request.method=='POST':
        plan.delete()
        return redirect('registration_plan_list')
    return render(request, template_name, {'object':rp})


#Client_Plan views
class Client_PlanForm(ModelForm):
    class Meta:
        model = Client_Plan
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def Client_Plan_list(request, template_name='core/client_plan_list.html'):
    c_plans = Client_Plan.objects.all()
    data = {}
    data['object_list'] = c_plans
    return render(request, template_name, data)


@login_required
def Client_Plan_create(request, template_name='core/client_plan_form.html'):
    form = Client_PlanForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_plan_list')
    return render(request, template_name, {'form':form})


@login_required
def Client_Plan_update(request, pk, template_name='core/client_plan_form.html'):
    c_plan = get_object_or_404(Client_Plan, pk=pk)
    form =Client_PlanForm(request.POST or None, instance=c_plan)
    if form.is_valid():
        form.save()
        return redirect('client_plan_list')
    return render(request, template_name, {'form':form})


@login_required
def Client_Plan_delete(request, pk, template_name='core/client_plan_confirm_delete.html'):
    c_plan = get_object_or_404(Client_Plan, pk=pk)
    if request.method=='POST':
        c_plan.delete()
        return redirect('client_plan_list')
    return render(request, template_name, {'object':c_plan})


#Invoice views
# class InvoiceForm(ModelForm):
#     class Meta:
#         model = Invoice
#     helper = FormHelper()
#     helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


# @login_required
# def Invoice_list(request, template_name='core/invoice_list.html'):
#     invoices = Invoice.objects.all()
#     data = {}
#     data['object_list'] = invoices
#     return render(request, template_name, data)


# @login_required
# def Invoice_create(request, template_name='core/invoice_form.html'):
#     form = InvoiceForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('invoice_list')
#     return render(request, template_name, {'form':form})


# @login_required
# def Invoice_update(request, pk, template_name='core/invoice_form.html'):
#     invoice = get_object_or_404(Invoice, pk=pk)
#     form =InvoiceForm(request.POST or None, instance=invoice)
#     if form.is_valid():
#         form.save()
#         return redirect('invoice_list')
#     return render(request, template_name, {'form':form})


@login_required
def Invoice_delete(request, pk, template_name='core/invoice_confirm_delete.html'):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method=='POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, template_name, {'object':invoice})


#Order views
class OrderForm(ModelForm):
    class Meta:
        model = Order
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def orders_list(request, template_name='core/order_list.html'):
    orders = Order.objects.all()
    data = {}
    data['object_list'] = orders
    return render(request, template_name, data)


@login_required
def order_create(request, template_name='core/order_form.html'):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('orders_list')
    return render(request, template_name, {'form':form})


@login_required
def order_update(request, pk, template_name='core/order_form.html'):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('orders_list')
    return render(request, template_name, {'form':form})


@login_required
def order_delete(request, pk, template_name='core/order_confirm_delete.html'):
    order = get_object_or_404(Order, pk=pk)
    if request.method=='POST':
        order.delete()
        return redirect('orders_list')
    return render(request, template_name, {'object':order})


#Supplier views
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def Supplier_list(request, template_name='core/supplier_list.html'):
    suppliers = Supplier.objects.all()
    data = {}
    data['object_list'] = suppliers
    return render(request, template_name, data)


@login_required
def Supplier_create(request, template_name='core/supplier_form.html'):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, template_name, {'form':form})


@login_required
def Supplier_update(request, pk, template_name='core/supplier_form.html'):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid():
        form.save()
        return redirect('supplier_list')
    return render(request, template_name, {'form':form})


@login_required
def Supplier_delete(request, pk, template_name='core/supplier_confirm_delete.html'):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method=='POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, template_name, {'object':supplier})


#Customer views
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required

def Customer_list(request, template_name='core/customer_list.html'):
    customers = Customer.objects.all()
    data = {}
    data['object_list'] = customers
    return render(request, template_name, data)


# @login_required
# def Customer_create(request, template_name='core/customer_form.html'):
#     form = CustomerForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         user = User.objects.create_user(username=form.data['f_name'],
#         email=form.data['email_address'],
#         password=form.data['password'])
#         user.is_staff = False
#         user.save()
#         return redirect('customer_list')
#     return render(request, template_name, {'form':form})

@login_required

def Customer_update(request, pk, template_name='core/customer_form.html'):
    customers = get_object_or_404(Customer, pk=pk)
    form =CustomerForm(request.POST or None, instance=customers)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    return render(request, template_name, {'form':form})


@login_required
def Customer_delete(request, pk, template_name='core/customer_confirm_delete.html'):
    customers = get_object_or_404(Customer, pk=pk)
    if request.method=='POST':
        customers.delete()
        return redirect('customer_list')
    return render(request, template_name, {'object':customers})
# cart views
class CartForm(ModelForm):
    class Meta:
        model = Cart
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def Cart_list(request, template_name='core/cart_list.html'):
    carts = Cart.objects.all()
    data = {}
    data['object_list'] = carts
    return render(request, template_name, data)


@login_required
def Cart_create(request, template_name='core/cart_form.html'):
    form = CartForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cart_list')
    return render(request, template_name, {'form':form})

def cart_context_data(request, context=None):
    ctxt_dict = {}
    ctxt_dict['current_logged_user'] = request.user

    if Account.objects.filter(pk=request.user.id).exists() is False:
        Account.objects.create(name=request.user.username,
                                account_number=10001, nature='DEB',
                                )

    else:
        pass

    if Customer.objects.filter(pk=request.user.id).exists() is False:
        Customer.objects.create(c_user=User.objects.get(pk=request.user.id),
                                f_name=request.user.first_name,
                                l_name=request.user.last_name,
                                email_address=request.user.email,
                                c_account=Account.objects.get(pk=request.user.id),
                                )
    else: pass


    if Cart.objects.filter(pk=request.user.id).exists() is False:
        Cart.objects.create(customer_ID=Customer.objects.get(pk=request.user.id))
    else: pass

    if Invoice.objects.filter(pk=request.user.id).exists() is False:
        Invoice.objects.create()
    else: pass

    if CustomerCart.objects.filter(pk=request.user.id).exists() is False:
        CustomerCart.objects.create(customer_ID=Customer.objects.get(pk=request.user.id),
                                    cart_ID=Cart.objects.get(pk=request.user.id)
                                    )
    else: pass

    if CustomerOrder.objects.filter(pk=request.user.id).exists() is False:
        CustomerOrder.objects.create(customer_ID=Customer.objects.get(pk=request.user.id))
    else: pass

    if CustomerInvoice.objects.filter(pk=request.user.id).exists() is False:
        CustomerInvoice.objects.create(customer_order=CustomerOrder.objects.get(pk=request.user.id),
                                        invoice = Invoice.objects.get(pk=request.user.id),
                                        )
    else: pass

    cart = Cart.objects.get(pk=request.user.id)
    invoice = Invoice.objects.get(pk=request.user.id)
    ctxt_dict['customer'] = Customer.objects.get(pk=request.user.id)
    ctxt_dict['customer_cart'] = CustomerCart.objects.get(pk=request.user.id)
    ctxt_dict['customer_order'] = CustomerOrder.objects.get(pk=request.user.id)
    ctxt_dict['customer_invoice'] = CustomerInvoice.objects.get(pk=request.user.id)
    ctxt_dict['products'] = Product.objects.all()
    ctxt_dict['cart'] = Cart.objects.get(pk=request.user.id)
    ctxt_dict['cartItems'] = cart.cartitem_set.all()
    ctxt_dict['orders'] = Order.objects.all()
    ctxt_dict['invoiceItems'] = invoice.objects.all()
    context = RequestContext(request, ctxt_dict) if context is None \
    else context.update(ctxt_dict)
    return context

@login_required
def Cart_update(request, pk, template_name='core/cart_form.html'):
    cart = get_object_or_404(Cart, pk=pk)
    form =CartForm(request.POST or None, instance=cart)
    if form.is_valid():
        form.save()
        return redirect('cart_list')
    return render(request, template_name, {'form':form})


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem

    helper = FormHelper()
    helper.add_input(Submit('Add to Cart', 'Add to Cart', css_class='btn-primary'))


@login_required
def CustomerCart_update(request, pk, template_name='core/customercart_form.html'):
    ccart = get_object_or_404(CustomerCart, pk=pk)
    form =CustomerCartForm(request.POST or None, instance=ccart)
    if form.is_valid():
        form.save()
        return redirect('ccart_list')
    return render(request, template_name, {'form':form})


@login_required
def cart(request, template_name = 'core/cart.html'):
    context = cart_context_data(request)
    return render_to_response(template_name, {}, context_instance=context)


@login_required
def shop(request, template_name='core/shop.html'):
    context = cart_context_data(request)
    return render(request, template_name, context)


#customer invoice views
class CustomerInvoiceForm(ModelForm):
    class Meta:
        model = CustomerInvoice
    helper = FormHelper()
    helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))


@login_required
def CustomerInvoice_create(request, template_name='core/customerinvoice_form.html'):
    form = CustomerInvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customerinvoice_list')
    return render(request, template_name, {'form':form})


@login_required
def CustomerInvoice_update(request, pk, template_name='core/customerinvoice_form.html'):
    cinv = get_object_or_404(CustomerInvoice, pk=pk)
    form =CustomerInvoiceForm(request.POST or None, instance=cinv)
    if form.is_valid():
        form.save()
        return redirect('customerinvoice_list')
    return render(request, template_name, {'form':form})


@login_required
def CustomerInvoice_delete(request, pk, template_name='core/customerinvoice_confirm_delete.html'):
    cinv = get_object_or_404(CustomerInvoice, pk=pk)
    if request.method=='POST':
        cinv.delete()
        return redirect('customerinvoice_list')
    return render(request, template_name, {'object':cinv})

# cusromer order views
# class CustomerOrderForm(ModelForm):
#     class Meta:
#         model = CustomerOrder
#     helper = FormHelper()
#     helper.add_input(Submit('Add/Update', 'Add/Update', css_class='btn-primary'))
#
#
# @login_required
# def CustomerOrder_list(request, template_name='core/customerorder_list.html'):
#     corders = CustomerOrder.objects.all()
#     data = {}
#     data['object_list'] = corders
#     return render(request, template_name, data)
#
#
# @login_required
# def CustomerOrder_create(request, template_name='core/customerorder_form.html'):
#     form = CustomerOrderForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('corder_list')
#     return render(request, template_name, {'form':form})
#
#
# @login_required
# def CustomerOrder_update(request, pk, template_name='core/customerorder_form.html'):
#     corder = get_object_or_404(CustomerOrder, pk=pk)
#     form =CustomerOrderForm(request.POST or None, instance=corder)
#     if form.is_valid():
#         form.save()
#         return redirect('corder_list')
#     return render(request, template_name, {'form':form})
#
#
# @login_required
# def CustomerOrder_delete(request, pk, template_name='core/customerorder_confirm_delete.html'):
#     corder = get_object_or_404(CustomerOrder, pk=pk)
#     if request.method=='POST':
#         corder.delete()
#         return redirect('corder_list')
#     return render(request, template_name, {'object':corder})


#######
@login_required
def add_to_cart(request, pk, template_name='core/shop.html'):
    product = get_object_or_404(Product, pk=pk)
    context = cart_context_data(request)
    if CartItem.objects.filter(product_name = product).exists() is False:
            cartitem = CartItem(cart_ID = context['cart'], product_name = product , quantity = 1)
            cartitem.save()
            print cartitem
    else: pass
    redirect('shop')
    return render_to_response(template_name, {'product': product}, context_instance=context)
#######

#######
@login_required
def order(request, pk, template_name='core/cart.html'):
    cart = get_object_or_404(Cart, pk=pk)
    customerinvoice = get_object_or_404(CustomerInvoice, pk=pk)
    context = cart_context_data(request)
    product_names = []
    product_quantities = []
    product_prices = []
    cartitem_subtotal = []
    for item in CartItem.objects.all():
        for product in Product.objects.all():
            if item.product_name == product:
                product_names.append(product.Product_Name)
                product_quantities.append(item.quantity)
                product_prices.append(product.Product_Price)
                cartitem_subtotal.append(product.Product_Price * item.quantity)

    for cartitem in context['cartItems']:
        for product in product_names:
            for qt in product_quantities:
                for cti_sub in cartitem_subtotal:
                    if cartitem.product_name == product:
                        if InvoiceItem.objects.filter(invoice_ID=request.user.id).exists() is False:
                            invoiceitem = InvoiceItem(invoice_ID=request.user.id, 
                                                product_name= product,
                                                quantity= qt,
                                                item_subtotal= cti_sub,
                                                )
                            invoiceitem.save()
    
    if CustomerOrder.objects.filter(customer_ID = context['customer']).exists() is False:
        customerorder = CustomerOrder(customer_ID = context['customer'], cart_ID = cart)
        customerorder.save()
    else:
        CustomerOrder.objects.update(customer_ID = context['customer'], cart_ID = cart)
        render_to_response(template_name, {'cart': cart}, context_instance=context)
        print product_names 
        print product_quantities 
        print product_prices 
        print cartitem_subtotal 

    return redirect('shop')
#######

#######
@login_required
def invoice(request, pk, template_name='core/invoice.html'):
    customerorder = get_object_or_404(CustomerOrder, pk=pk)
    customerinvoice = get_object_or_404(CustomerInvoice, pk=pk)
    context = cart_context_data(request)
    invoiceitem = InvoiceItem.objects.all().filter(invoice_ID=customerinvoice.id)

    return render_to_response(template_name, {'customerinvoice': customerinvoice,
                                            'customerorder': customerorder,
                                            'invoiceitem': invoiceitem,
                                            
                                            },
                                                context_instance=context)
#######
    # invoice = Invoice(invoiceitem, total)
    # customerinvoice = CustomerInvoice(customer_order, invoice)
    # InvoiceItem(product_name = Product.objects.get(pk=1), quantity = 1, item_subtotal = 10)
    # total =
    # item_subtotal
    # print invoice.total
    # print Cart.objects.get(pk=1).cartitem_set.all().values_list('product_name')
    # print Cart.objects.get(pk=1).cartitem_set.all().values_list('quantity')
    # print Cart.objects.get(pk=1).cartitem_set.all()