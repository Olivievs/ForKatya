# Generated by Django 3.2.4 on 2023-05-22 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0002_auto_20230522_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatclassification',
            name='CAEC',
            field=models.CharField(blank=True, choices=[('0', 'нет'), ('1', 'иногда'), ('2', 'часто'), ('3', 'всегда')], default='0', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='CALC',
            field=models.CharField(blank=True, choices=[('0', 'нет'), ('1', 'иногда'), ('2', 'часто'), ('3', 'всегда')], default='0', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='CH2O',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='FAF',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='FAVC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='FCVC',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='MTRANS',
            field=models.CharField(blank=True, choices=[('0', 'на машине'), ('1', 'на мотоцикле'), ('2', 'на велосипеде'), ('3', 'на общественном транспорте'), ('4', 'пешком')], default='4', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='NCP',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='SCC',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='SMOKE',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='TUE',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='age',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='family_history_with_overweight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
