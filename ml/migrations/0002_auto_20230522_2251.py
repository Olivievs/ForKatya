# Generated by Django 3.2.4 on 2023-05-22 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatclassification',
            name='CAEC',
            field=models.CharField(choices=[('0', 'нет'), ('1', 'иногда'), ('2', 'часто'), ('3', 'всегда')], default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='CALC',
            field=models.CharField(choices=[('0', 'нет'), ('1', 'иногда'), ('2', 'часто'), ('3', 'всегда')], default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='MTRANS',
            field=models.CharField(choices=[('0', 'на машине'), ('1', 'на мотоцикле'), ('2', 'на велосипеде'), ('3', 'на общественном транспорте'), ('4', 'пешком')], default='4', max_length=255),
        ),
        migrations.AlterField(
            model_name='fatclassification',
            name='nobeyesdad',
            field=models.CharField(blank=True, choices=[('0', 'недостаточный вес'), ('1', 'нормальный вес'), ('2', 'избыточный вес 1-й стадии'), ('3', 'избыточный вес 2-й стадии'), ('4', 'ожирение 1-й стадии'), ('5', 'ожирение 2-й стадии'), ('6', 'ожирение 3-й стадии')], default='', max_length=255, null=True),
        ),
    ]