from django.contrib import admin
from fulfillment.models import Fulfillment_Entry ,Sales_Order, Sales_Invoice

# Register your models here.
class FulfillmentAdmin(admin.ModelAdmin):
  fieldsets=[
  ('sales order',{'fields':['so_id']}),
  (None,{'fields':['deliverd']}),
  ('date information',{'fields':['date_time']}),
  ]
  list_display =('so_id','deliverd','date_time')
  list_filter=['date_time']
  search_fields = ['so_id']
admin.site.register(Fulfillment_Entry, FulfillmentAdmin)


class Sales_InvoiceAdmin(admin.ModelAdmin):
  fieldsets=[
  #('sales order',{'fields':['so_id']}),
  (None,{'fields':['customer']}),
  ('date information',{'fields':['price']}),
  ('date information',{'fields':['date_time']}),
  ]
  list_display =('customer','price','date_time')
  list_filter=['date_time']
  search_fields = ['customer']
admin.site.register(Sales_Invoice, Sales_InvoiceAdmin)


class Sales_OrderAdmin(admin.ModelAdmin):
  fieldsets=[
  #('sales order',{'fields':['so_id']}),
  (None,{'fields':['product']}),
  (None,{'fields':['warehouse']}),
  (None,{'fields':['supplier']}),
  (None,{'fields':['date']}),
  (None,{'fields':['quantity']}),
  ]
  list_display =('product','warehouse','date')
  list_filter=['date']
  search_fields = ['product']
admin.site.register(Sales_Order, Sales_OrderAdmin)
