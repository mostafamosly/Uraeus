from django.conf.urls import patterns, url

from product import views

urlpatterns = patterns('',
  url(r'^list$', views.product_list, name='product_list'),
  url(r'^add$', views.product_create, name='porduct_create'),
  url(r'^update/(?P<pk>\d+)$', views.product_update, name='product_update'),
  url(r'^delete/(?P<pk>\d+)$', views.product_delete, name='product_delete'),
)
