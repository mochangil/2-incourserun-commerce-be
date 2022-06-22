from django.contrib import admin
from app.product.models import Product


@admin.register(Product)
class ProduectAdmin(admin.ModelAdmin):
    pass
