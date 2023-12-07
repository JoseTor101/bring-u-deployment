from django.contrib import admin
from .models import Business, Product, Request, Delivery, HistoryRequest, HistoryDelivery
# Register your models here.
admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Request)
admin.site.register(Delivery)
admin.site.register(HistoryRequest)
admin.site.register(HistoryDelivery)