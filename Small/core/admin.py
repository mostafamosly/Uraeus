from django.contrib import admin
from core.models import *

# Register your models here.


admin.site.register(CustomerOrder)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Client_Plan)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(CustomerCart)
admin.site.register(CustomerInvoice)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)

#admin.site.register(Registration_Plan)
#admin.site.register(Client_Plan)
# class Client_PlanAdmin(admin.ModelAdmin):
#   fieldsets=[
#   ('registration_date',{'fields':['registration_date']}),
#   ('registration_expirationDate',{'fields':['registration_expirationDate']}),
#   ('Module',{'fields':['module']}),
#   ('registration_plan',{'fields':['registration_plan']}),
#   ('user',{'fields':['user']}),
#   ]
#   list_display = ('registration_date','registration_expirationDate','module','registration_plan','user')
#   list_filter=['registration_date']
#   search_fields = ['user']
# admin.site.register(Client_Plan, Client_PlanAdmin)


# class Registration_PlanAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Name', {'fields': ['registration_plan_name']}),
#         ('Period', {'fields': ['registration_plan_Period']}),
#         ('Price', {'fields': ['registration_plan_Price']}),
#     ]
#     list_display = ('registration_plan_name', 'registration_plan_Period', 'registration_plan_Price')
#     search_fields = ['registration_plan_name']
#     list_filter=['registration_plan_Period']

# admin.site.register(Registration_Plan , Registration_PlanAdmin)

# class ModuleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Module Name', {'fields': ['module_name']}),
#         ('Enabled', {'fields': ['Enabled']}),
#     ]
#     list_display = ('id', 'module_name', 'Enabled')
#     search_fields = ['module_name']

# admin.site.register(Module, ModuleAdmin)

# class SupplierAdmin(admin.ModelAdmin):
#   fieldsets=[
#   ('NAME',{'fields':['s_name']}),
#   ('Email',{'fields':['s_email']}),
#   ('phone',{'fields':['s_phone']}),
#   ('fax',{'fields':['s_fax']}),
#   ('address',{'fields':['address']}),
#   ('supplier account',{'fields':['s_account']}),
#   ]
#   list_display = ('s_name','s_email','s_phone','s_fax','address')
#   list_filter=['s_name']
#   search_fields = ['s_phone']

# admin.site.register(Supplier, SupplierAdmin)

# class CustomerAdmin(admin.ModelAdmin):
#   fieldsets=[
#   ('first name',{'fields':['f_name']}),
#   ('last name',{'fields':['l_name']}),
#   ('Email',{'fields':['email_address']}),
#   ('phone',{'fields':['phone']}),
#   ('address',{'fields':['address']}),
#   ('customer account',{'fields':['c_account']}),
#   ]
#   list_display = ('f_name','l_name','email_address','phone','address')
#   list_filter=['phone']
#   search_fields = ['email_address']
# admin.site.register(Customer, CustomerAdmin)


# class InvoiceAdmin(admin.ModelAdmin):
#   fieldsets=[
#   ('Product',{'fields':['product_name']}),
#   ('Quantity',{'fields':['quantity']}),
#   ('price',{'fields':['pro_price']}),
#   ('Date',{'fields':['datetimestamp']}),
#   ]
#   list_display = ('product_name','quantity','pro_price')
#   list_filter=['product_name']
#   search_fields = ['product_name']
# admin.site.register(Invoice , InvoiceAdmin)


# class OrderAdmin(admin.ModelAdmin):
#   fieldsets=[
#   ('Product',{'fields':['product_name']}),
#   ('Quantity',{'fields':['quantity']}),
#   ('Date order',{'fields':['date_ordered']}),
#   ('Delivery-Date',{'fields':['delivery_date']}),
#   #('payment_deadline',{'fields':['payment_deadline']}),
#   ]
#   list_display = ('product_name','quantity','date_ordered')
#   list_filter=['product_name']
#   search_fields = ['date_ordered']
# admin.site.register(Order , OrderAdmin)
