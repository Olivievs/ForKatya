from django.contrib import admin

# Register your models here.

from .models import TextTranslationResult

@admin.register(TextTranslationResult)
class TextTranslationResultAdmin(admin.ModelAdmin):
    pass