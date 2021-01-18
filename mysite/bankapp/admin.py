from django.contrib import admin
from .models import Bank


@admin.register(Bank)
class BankAdmin (admin.ModelAdmin):
    list_display = ['id', 'contact_number', 'name', 'created_at', 'updated_at']

