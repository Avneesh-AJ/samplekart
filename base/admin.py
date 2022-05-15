from django.contrib import admin
from base import models

# Register your models here.
admin.site.register([
    models.Product,
    models.Review,
    models.Order,
    models.OrderItem,
    models.ShippingAddress
])