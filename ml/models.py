from django.db import models

class Frequency(models.TextChoices):
    NO = 0, "нет"
    SOMETIMES = 1, "иногда"
    FREQUENTLY = 2, "часто"
    ALWAYS = 3, "всегда"

class Transport(models.TextChoices):
    Automobile = 0, "на машине"
    Motorbike = 1, "на мотоцикле"
    Bike = 2, "на велосипеде"
    Public_Transportation = 3, "на общественном транспорте"
    Walking = 4, "пешком"

class NObeyesdad(models.TextChoices):
    Insufficient_Weight = 0, "недостаточный вес"
    Normal_Weight = 1, "нормальный вес"
    Overweight_Level_I = 2, "избыточный вес 1-й стадии"
    Overweight_Level_II = 3, "избыточный вес 2-й стадии"
    Obesity_Type_I = 4, "ожирение 1-й стадии"
    Obesity_Type_II = 5, "ожирение 2-й стадии"
    Obesity_Type_III = 6, "ожирение 3-й стадии"

class FatClassification(models.Model):

    model_id = models.BigAutoField(primary_key=True)
    gender = models.IntegerField(blank=True, null=True)
    age = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    family_history_with_overweight = models.IntegerField(blank=True, null=True)
    FAVC = models.IntegerField(blank=True, null=True)
    FCVC = models.FloatField(blank=True, null=True)
    NCP = models.FloatField(blank=True, null=True)
    CAEC = models.CharField(
        max_length=255,
        choices = Frequency.choices,
        default = Frequency.NO,
        blank=True, null=True
        )
    SMOKE = models.IntegerField(blank=True, null=True)
    CH2O = models.FloatField(blank=True, null=True)
    SCC = models.IntegerField(blank=True, null=True)
    FAF = models.FloatField(blank=True, null=True)
    TUE = models.FloatField(blank=True, null=True)
    CALC = models.CharField(
        max_length=255,
        choices = Frequency.choices,
        default = Frequency.NO,
        blank=True, null=True
        )
    MTRANS = models.CharField(
        max_length=255,
        choices = Transport.choices,
        default = Transport.Walking,
        blank=True, null=True
    )
    nobeyesdad = models.CharField(
        max_length=255,
        choices = NObeyesdad.choices,
        blank = True,
        null = True,
        default = ""
    )

    def __init__(self, *args, **kwargs):
        l = []
        for el in args:
            l = el
        self.gender = l[0]
        self.age = l[1]
        self.height = l[2]
        self.weight = l[3]
        self.family_history_with_overweight = l[4]
        self.FAVC = l[5]
        self.FCVC = l[6]
        self.NCP = l[7]
        self.CAEC = l[8]
        self.SMOKE = l[9]
        self.CH2O = l[10]
        self.SCC = l[11]
        self.FAF = l[12]
        self.TUE = l[13]
        self.CALC = l[14]
        self.MTRANS = l[15]
        super(FatClassification, self).__init__()

    @staticmethod
    def to_model_style(arr):
        freq = list(Frequency)
        trans = list(Transport)
        l = []
        if arr[0]=="Female":
            l.append(0)
        else:
            l.append(1)
        for i in range(1, 4):
            l.append(float(arr[i]))
        if arr[4]=="yes":
            l.append(1)
        else:
            l.append(0)
        if arr[5]=="yes":
            l.append(1)
        else:
            l.append(0)
        for i in range(6, 8):
            l.append(float(arr[i]))
        l.append(freq[int(arr[8])].value[0])
        if arr[9]=="yes":
            l.append(1)
        else:
            l.append(0)
        l.append(float(arr[10]))
        if arr[11]=="yes":
            l.append(1)
        else:
            l.append(0)
        for i in range(12, 14):
            l.append(arr[i])
        l.append(freq[int(arr[14])].value[0])
        l.append(trans[int(arr[8])].value[0])
        return l

    def analyze(self, result):
        nob = list(NObeyesdad)
        self.nobeyesdad = nob[result].name

    class Meta:
        verbose_name = "Данные о человеке для классификации"

    

