from django.apps import AppConfig

##########################################
#   CONFIG CLASS
##########################################
# defines the application name as shopping, same as folder and in urls.py reference
class ShoppingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping'
