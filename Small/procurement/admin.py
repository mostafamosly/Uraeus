from django.contrib import admin
from procurement.models import *
# Register your models here.
class ProcurementAdmin(admin.ModelAdmin):
  fieldsets=[
  ('supplier', {'fields': ['supplier']}),
  ('product', {'fields': ['quantity']}),
  ('product', {'fields': ['product']}),
  ('pi', {'fields': ['pi_id']}),
  ('recived', {'fields':[ 'recived']}),
  ('date information', {'fields':['date_time']}),
  ]
  list_display = ('supplier', 'product', 'pi_id', 'recived', 'date_time')
  list_filter = ['date_time']
  search_fields = ['product_id']
admin.site.register(Procurement, ProcurementAdmin)

class PurchaseInvoiceAdmin(admin.ModelAdmin):
  fieldsets=[
  ('supplier', {'fields': ['s_id']}),
  ('Paid', {'fields':[ 'paid']}),
  ('date information', {'fields':['date_time']}),
  ]
  list_display = ('s_id','paid','date_time')
  list_filter = ['date_time']
  search_fields = ['s_id']
admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)

class PurchaseRequisionAdmin(admin.ModelAdmin):
  fieldsets=[
  ('product', {'fields': ['product']}),
  ('status', {'fields':[ 'status']}),
  ('date information', {'fields':['date_time']}),
  ]
  list_display = ('product','status','date_time')
  list_filter = ['status']
  search_fields = ['date_time']
admin.site.register(PurchaseRequision , PurchaseRequisionAdmin)

class PurchaseOrderAdmin(admin.ModelAdmin):
    fieldsets=[
    ('', {'fields': ['prq_id']}),
    #('q_id', {'fields':['q_id']}),
    ('', {'fields':['payment_terms']}),
    ('date information', {'fields':['date_time']}),
    ]
    list_display = ('prq_id','date_time')
    list_filter = ['date_time']
    search_fields = ['prq_id']
admin.site.register(PurchaseOrder ,PurchaseOrderAdmin)
