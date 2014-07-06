from django.conf.urls import patterns, url

from fulfillment import views

urlpatterns = patterns('',
  url(r'^fulfillment_list$', views.fulfillment_entrylist, name='fulfillment_list'),
  url(r'^fulfillment_add$', views.fulfillment_entrycreate, name='fulfillment_create'),
  url(r'^fulfillment_update/(?P<pk>\d+)$', views.fulfillment_entryupdate, name='fulfillment_update'),
  url(r'^fulfillment_delete/(?P<pk>\d+)$', views.fulfillment_entrydelete, name='fulfillment_delete'),


  url(r'^Sales_Invoice_list$', views.Sales_Invoicelist, name='Sales_Invoice_list'),
  url(r'^Sales_Invoice_create$', views.Sales_Invoicecreate, name='Sales_Invoice_create'),
  url(r'^Sales_Invoice_update/(?P<pk>\d+)$', views.Sales_Invoiceupdate, name='Sales_Invoice_update'),
  url(r'^Sales_Invoice_delete/(?P<pk>\d+)$', views.Sales_Invoicedelete, name='Sales_Invoice_delete'),


  url(r'^Sales_order_list$', views.Sales_Orderlist, name='Sales_order_list'),
  url(r'^Sales_order_create$', views.Sales_Ordercreate, name='Sales_order_create'),
  url(r'^Sales_order_update/(?P<pk>\d+)$', views.Sales_Orderupdate, name='Sales_order_update'),
  url(r'^Sales_order_delete/(?P<pk>\d+)$', views.Sales_Orderdelete, name='Sales_order_delete'),
)
