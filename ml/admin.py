from django.contrib import admin

# Register your models here.

from .models import FatClassification

@admin.register(FatClassification)
class FatClassificationAdmin(admin.ModelAdmin):
    pass