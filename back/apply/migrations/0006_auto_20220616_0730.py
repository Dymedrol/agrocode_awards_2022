# Generated by Django 3.2.13 on 2022-06-16 04:30

from django.db import migrations, models

def cut_fields(apps, schema_editor):
    AgroLaunch = apps.get_model('apply', 'AgroLaunch')
    AgroLaunch.objects.all().update(project_stage='1')
    models_set = (
        'AgroMachinery',
        'AgroDigital',
        'FutureFood',
        'MadeInRussia',
        'AgroLaunch',
    )
    for model_name in models_set:
        model = apps.get_model('apply', model_name)
        model.objects.all().update(release_year='2020')


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_auto_20220615_1426'),
    ]

    operations = [
        migrations.RunPython(cut_fields),
        migrations.AlterField(
            model_name='agrodigital',
            name='release_year',
            field=models.CharField(choices=[('before_2018', 'ранее 2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], db_index=True, max_length=11, verbose_name='Год реализации кейса'),
        ),
        migrations.AlterField(
            model_name='agrolaunch',
            name='project_stage',
            field=models.CharField(choices=[('1', 'MVP (работающий прототип без продаж)'), ('2', 'Работающая технология с подтвержденным спросом (есть пилоты или первые клиенты)'), ('3', 'Работающий бизнес (есть клиенты, операционная безубыточность)'), ('4', 'Зрелая компания с прибылью')], db_index=True, max_length=1, verbose_name='Стадия развития'),
        ),
        migrations.AlterField(
            model_name='agrolaunch',
            name='release_year',
            field=models.CharField(choices=[('before_2018', 'ранее 2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], db_index=True, max_length=11, verbose_name='Год запуска кейса'),
        ),
        migrations.AlterField(
            model_name='agromachinery',
            name='release_year',
            field=models.CharField(choices=[('before_2018', 'ранее 2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], db_index=True, max_length=11, verbose_name='Год реализации кейса'),
        ),
        migrations.AlterField(
            model_name='futurefood',
            name='release_year',
            field=models.CharField(choices=[('before_2018', 'ранее 2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], db_index=True, max_length=11, verbose_name='Год реализации кейса'),
        ),
        migrations.AlterField(
            model_name='madeinrussia',
            name='release_year',
            field=models.CharField(choices=[('before_2018', 'ранее 2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], db_index=True, max_length=11, verbose_name='Год запуска кейса'),
        ),
    ]
