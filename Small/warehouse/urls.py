from django.conf.urls import patterns, url

from warehouse import views

urlpatterns = patterns('',
  url(r'^warehouse_list$', views.warehouse_list, name='warehouse_list'),
  url(r'^warehouse_add$', views.warehouse_create, name='warehouse_create'),
  url(r'^warehouse_update/(?P<pk>\d+)$', views.warehouse_update, name='warehouse_update'),
  url(r'^warehouse_delete/(?P<pk>\d+)$', views.warehouse_delete, name='warehouse_delete'),


  url(r'^section_list$', views.section_list, name='section_list'),
  url(r'^section_add$', views.section_create, name='section_create'),
  url(r'^section_update/(?P<pk>\d+)$', views.section_update, name='section_update'),
  url(r'^section_delete/(?P<pk>\d+)$', views.section_delete, name='section_delete'),


  url(r'^inventory_list$', views.inventory_list, name='inventory_list'),
  url(r'^inventory_add$', views.inventory_create, name='inventory_create'),
  url(r'^inventory_update/(?P<pk>\d+)$', views.inventory_update, name='inventory_update'),
  url(r'^inventory_delete/(?P<pk>\d+)$', views.inventory_delete, name='inventory_delete'),
)
