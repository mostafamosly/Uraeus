from django.contrib import admin
from accounting.models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Asset)
admin.site.register(BalanceSheet)
admin.site.register(Equity)
admin.site.register(Liability)
