# Generated by Django 4.0.5 on 2022-06-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entercoeff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coefficient',
            name='b_coef',
            field=models.FloatField(default=0, verbose_name='Коэфф. b'),
        ),
        migrations.AddField(
            model_name='coefficient',
            name='c_coef',
            field=models.FloatField(default=0, verbose_name='Коэфф. c'),
        ),
        migrations.AlterField(
            model_name='coefficient',
            name='a_coef',
            field=models.FloatField(default=0, verbose_name='Коэфф. a'),
        ),
    ]
