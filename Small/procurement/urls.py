from django.conf.urls import patterns, url
from procurement import views

urlpatterns = patterns('',
  url(r'^procurement_list$', views.Procurement_list, name='procurement_list'),
  url(r'^procurement_add$', views.Procurement_create, name='procurement_create'),
  url(r'^procurement_update/(?P<pk>\d+)$', views.Procurement_update, name='procurement_update'),
  url(r'^procurement_delete/(?P<pk>\d+)$', views.Procurement_delete, name='procurement_delete'),

  url(r'^invoice_list$', views.PurchaseInvoice_list, name='purchaseinvoice_list'),
  url(r'^invoice_add$', views.PurchaseInvoice_create, name='purchaseinvoice_create'),
  url(r'^invoice_update/(?P<pk>\d+)$', views.PurchaseInvoice_update, name='purchaseinvoice_update'),
  url(r'^invoice_delete/(?P<pk>\d+)$', views.PurchaseInvoice_delete, name='purchaseinvoice_delete'),

#requist
  url(r'^requision_list$', views.purchaserequision_list, name='purchaserequision_list'),
  url(r'^requision_add$', views.purchaserequision_create, name='purchaserequision_create'),
  url(r'^requision_update/(?P<pk>\d+)$', views.purchaserequision_update, name='purchaserequision_update'),
  url(r'^requision_delete/(?P<pk>\d+)$', views.purchaserequision_delete, name='purchaserequision_delete'),
#order
  url(r'^order_list$', views.PurchaseOrder_list, name='purchaseorder_list'),
  url(r'^order_add$', views.PurchaseOrder_create, name='purchaseorder_create'),
  url(r'^order_update/(?P<pk>\d+)$', views.PurchaseOrder_update, name='purchaseorder_update'),
  url(r'^order_delete/(?P<pk>\d+)$', views.PurchaseOrder_delete, name='purchaseorder_delete'),

)
