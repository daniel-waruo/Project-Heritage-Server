from django.contrib import admin
from .models import PhClass


# Register your models here.
@admin.register(PhClass)
class PhClassModelAdmin(admin.ModelAdmin):
    pass
