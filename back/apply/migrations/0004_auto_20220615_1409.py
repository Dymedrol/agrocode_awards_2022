# Generated by Django 3.2.13 on 2022-06-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_merge_0002_auto_20220614_1405_0002_auto_20220615_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agrodigital',
            name='company_url',
            field=models.CharField(max_length=255, verbose_name='Сайт компании'),
        ),
        migrations.AlterField(
            model_name='agrohero',
            name='company_url',
            field=models.CharField(max_length=255, verbose_name='Сайт компании'),
        ),
        migrations.AlterField(
            model_name='agrolaunch',
            name='project_url',
            field=models.CharField(max_length=255, verbose_name='Сайт проекта'),
        ),
        migrations.AlterField(
            model_name='agromachinery',
            name='company_url',
            field=models.CharField(max_length=255, verbose_name='Сайт компании'),
        ),
        migrations.AlterField(
            model_name='futurefood',
            name='company_url',
            field=models.CharField(max_length=255, verbose_name='Сайт компании'),
        ),
        migrations.AlterField(
            model_name='madeinrussia',
            name='company_url',
            field=models.CharField(max_length=255, verbose_name='Сайт компании'),
        ),
    ]
