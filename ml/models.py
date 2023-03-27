from django.db import models

class FatClassification(models.Model):
    model_id = models.BigAutoField(primary_key=True)
    gender = models.BooleanField()
    age = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    family_history_with_overweight = models.BooleanField()
    FAVC = models.BooleanField()
    FCVC = models.FloatField()
    NCP = models.FloatField()
    CAEC = models.CharField(
        choices = Frequency.choices,
        default = Frequency.NO
        )
    SMOKE = models.BooleanField()
    CH2O = models.FloatField()
    SCC = models.BooleanField()
    FAF = models.FloatField()
    TUE = models.FloatField()
    CALC = models.CharField(
        choices = Frequency.choices,
        default = Frequency.NO
        )
    MTRANS = models.CharField(
        choices = Transport.choices,
        default = Transport.Walking
    )
    nobeyesdad = models.CharField(
        choices = NObeyesdad.choices,
        blank = True,
        null = True,
        default = ""
    )

    class Meta:
        verbose_name = "Данные о человеке для классификации"

    
class Frequency(model.TextChoices):
    NO = 'no', "нет"
    SOMETIMES = "Sometimes", "иногда"
    FREQUENTLY = "Frequently", "часто"
    ALWAYS = "Always", "всегда"

class Transport(model.TextChoices):
    Automobile = "Automobile", "на машине"
    Motorbike = "Motorbike", "на мотоцикле"
    Bike = "Bike", "на велосипеде"
    Public_Transportation = "Public Transportation", "на общественном транспорте"
    Walking = "Walking", "пешком" 

class NObeyesdad(model.TextChoices):
    Insufficient_Weight = "Insufficient", "недостаточный вес"
    Normal_Weight = "Normal", "нормальный вес"
    Overweight_Level_I = "Overweight_I", "избыточный вес 1-й стадии"
    Overweight_Level_II = "Overweight_II", "избыточный вес 2-й стадии"
    Obesity_Type_I = "Obesity_I", "ожирение 1-й стадии"
    Obesity_Type_II = "Obesity_II", "ожирение 2-й стадии"
    Obesity_Type_III = "Obesity_III", "ожирение 3-й стадии"
