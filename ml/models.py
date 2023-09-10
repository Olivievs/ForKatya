from django.db import models

class TextTranslationResult(models.Model):
    id = models.BigAutoField(primary_key=True)
    input_text = models.CharField(max_length=255, blank=True, null=True)
    output_text = models.CharField(max_length=255, blank=True, null=True)

