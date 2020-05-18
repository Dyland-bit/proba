from django.contrib import admin

# Register your models here.
from .models import Files, Shops, Categorys, Subcategorys, Products, Buys


admin.site.register(Files)
admin.site.register(Shops)
admin.site.register(Categorys)
admin.site.register(Subcategorys)
admin.site.register(Products)
admin.site.register(Buys)