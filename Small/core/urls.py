from django.conf.urls import patterns, url
from core import views

urlpatterns = patterns('',
  url(r'^modules$', views.module_list, name='module_list'),
  url(r'^module/new/$', views.module_create, name='module_create'),
  url(r'^module_update/(?P<pk>\d+)$', views.module_update, name='module_update'),
  url(r'^module_delete/(?P<pk>\d+)$', views.module_delete, name='module_delete'),


  url(r'^registration_plans$', views.registration_plan_list, name='registration_plan_list'),
  url(r'^registration_plan/new/$', views.registration_plan_create, name='registration_plan_create'),
  url(r'^registration_plan_update/(?P<pk>\d+)$', views.registration_plan_update, name='registration_plan_update'),
  url(r'^registration_plan_delete/(?P<pk>\d+)$', views.registration_plan_delete, name='registration_plan_delete'),


  # url(r'^invoices$', views.Invoice_list, name='invoice_list'),
  # url(r'^invoice/new/$', views.Invoice_create, name='invoice_create'),
  # url(r'^invoice_update/(?P<pk>\d+)$', views.Invoice_update, name='invoice_update'),
  # url(r'^invoice_delete/(?P<pk>\d+)$', views.Invoice_delete, name='invoice_delete'),


  url(r'^client_plans$', views.Client_Plan_list, name='client_plan_list'),
  url(r'^client_plan/new$', views.Client_Plan_create, name='client_plan_create'),
  url(r'^client_plan_update/(?P<pk>\d+)$', views.Client_Plan_update, name='client_plan_update'),
  url(r'^client_plan_delete/(?P<pk>\d+)$', views.Client_Plan_delete, name='client_plan_delete'),


  url(r'^orders$',views.orders_list, name='orders_list'),
  url(r'^order/new/$',views.order_create, name='order_create'),
  url(r'^order/edit/(?P<pk>\d+)$',views.order_update, name='order_update'),
  url(r'^order/delete(?P<pk>\d+)$',views.order_delete, name='order_delete'),


  url(r'^suppliers$',views.Supplier_list, name='supplier_list'),
  url(r'^supplier/new/$',views.Supplier_create, name='supplier_create'),
  url(r'^supplier_update(?P<pk>\d+)$',views.Supplier_update, name='supplier_update'),
  url(r'^supplier_delete(?P<pk>\d+)$',views.Supplier_delete, name='supplier_delete'),

  # url(r'^customers$',views.Customer_list, name='customer_list'),
  # url(r'^customer/new/$',views.Customer_create, name='customer_create'),
  # url(r'^customer_update(?P<pk>\d+)$',views.Customer_update, name='customer_update'),
  # url(r'^customer_delete(?P<pk>\d+)$',views.Customer_delete, name='customer_delete'),

  url(r'^carts$',views.Cart_list, name='cart_list'),
  url(r'^cart/new/$',views.Cart_create, name='cart_create'),
  url(r'^cart/edit/(?P<pk>\d+)$',views.Cart_update, name='cart_update'),
  #url(r'^cart/delete(?P<pk>\d+)$',views.Cart_delete, name='cart_delete'),

  #url(r'^ccarts$',views.CustomerCart_list, name='ccart_list'),
  #url(r'^ccart/new/$',views.CustomerCart_create, name='ccart_create'),
  url(r'^ccart/edit/(?P<pk>\d+)$',views.CustomerCart_update, name='ccart_update'),
  #url(r'^ccart/delete(?P<pk>\d+)$',views.CustomerCart_delete, name='ccart_delete'),

  #url(r'^customerinvoices$',views.CustomerInvoice_list, name='customerinvoice_list'),
  url(r'^customerinvoice/new/$',views.CustomerInvoice_create, name='customerinvoice_create'),
  url(r'^customerinvoice/edit/(?P<pk>\d+)$',views.CustomerInvoice_update, name='customerinvoice_update'),
  url(r'^customerinvoice/delete(?P<pk>\d+)$',views.CustomerInvoice_delete, name='customerinvoice_delete'),

  # url(r'^customerorders$',views.CustomerOrder_list, name='corder_list'),
  # url(r'^customerorder/new/$',views.CustomerOrder_create, name='corder_create'),
  # url(r'^customerorder/edit/(?P<pk>\d+)$',views.CustomerOrder_update, name='corder_update'),
  # url(r'^customerorder/delete(?P<pk>\d+)$',views.CustomerOrder_delete, name='corder_delete'),

  url(r'^cart$',views.cart, name='cart'),
  url(r'^shop$',views.shop, name='shop'),
  url(r'^add_to_cart/(?P<pk>\d+)$',views.add_to_cart, name='add_to_cart'),
  url(r'^order/(?P<pk>\d+)$',views.order, name='order'),
  url(r'^invoice/(?P<pk>\d+)$',views.invoice, name='invoice'),

  )
