from django.contrib import admin
from product.models import Product
# Register your models here.
# class ProductAdmin(admin.ModelAdmin):

#   fieldsets=[
#   ('Name', {'fields': ['Product_Name']}),
#   ('Barcode', {'fields':['Barcode']}),
#   ('Nature', {'fields':['Product_Nature']}),
#   ('Quantity', {'fields':['Product_Quantity']}),
#   ('Price', {'fields':['Product_Price']}),
#   ]
#   list_display = ('Product_Name','Barcode','Product_Nature')
#   list_filter = ['Barcode']
#   search_fields = ['Product_Name']



admin.site.register(Product)
