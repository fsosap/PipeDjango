# Generated by Django 3.0.3 on 2020-03-04 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperatures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temperature',
            name='type',
        ),
        migrations.AlterField(
            model_name='temperature',
            name='value',
            field=models.IntegerField(verbose_name='Temperatura(Centigrados)'),
        ),
    ]