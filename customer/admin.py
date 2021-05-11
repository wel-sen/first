from django.contrib import admin

from .models import MenuItem, category, OrderModel
# Register your models here.

admin.site.register(MenuItem)
admin.site.register(category)
admin.site.register(OrderModel)