from django.contrib import admin
from warehouse.models import Warehouse , Warehouse_Section , inventory
# Register your models here.

class WarehouseAdmin(admin.ModelAdmin):

  fieldsets=[
  ('Name', {'fields': ['w_name']}),
  ('location', {'fields':['w_location']}),
  ('capacity', {'fields':['w_capacity']}),

  ]
  list_display = ('w_name','w_location','w_capacity')
  list_filter = ['w_location']
  search_fields = ['w_name']
admin.site.register(Warehouse , WarehouseAdmin)

class inventoryAdmin(admin.ModelAdmin):

  fieldsets=[
  ('product', {'fields':['product_name']}),
  ('quantity', {'fields':['quantity']}),
  ('quantity', {'fields':['supplier']}),
  ('w_house', {'fields':['w_house']}),
  ('save_quantity', {'fields':['save_quantity']}),
  ]
  list_display = ('product_name','quantity','save_quantity')
  list_filter = ['product_name']
  search_fields = ['w_name']
admin.site.register(inventory , inventoryAdmin)

class Warehouse_SectionAdmin(admin.ModelAdmin):

  fieldsets=[
  ('Name', {'fields': ['sec_name']}),
  ('capacity', {'fields':['sec_capacity']}),
  ('product', {'fields':['products']}),
  ('wharehouse', {'fields':['warehouse_ID']}),
  ]
  list_display = ('sec_name','sec_capacity','warehouse_ID')
  list_filter = ['sec_name']
  search_fields = ['warehouse_ID']
admin.site.register(Warehouse_Section , Warehouse_SectionAdmin)
