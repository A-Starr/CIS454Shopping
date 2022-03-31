from django.contrib import admin
from . import models

##########################################
#   SITE REGISTERS
##########################################

# Model for Product
admin.site.register(models.Product)

# Model for Customer
admin.site.register(models.Customer, admin.ModelAdmin)

# Model for Administrator
admin.site.register(models.Administrator, admin.ModelAdmin)

# Model for Company
admin.site.register(models.Company, admin.ModelAdmin)