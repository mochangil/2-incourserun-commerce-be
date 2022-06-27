from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Review information', {'fields': [
            "user",
            "product",
            "rating",
            "context",
        ]})
    ]

    list_display = (
        "user",
        "product",
        "rating",
        "context",
        "create_date"
    )