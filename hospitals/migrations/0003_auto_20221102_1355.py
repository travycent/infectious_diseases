# Generated by Django 3.2.10 on 2022-11-02 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_alter_hospitalsmodel_assigned_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='districtmodel',
            options={'verbose_name_plural': 'District Details'},
        ),
        migrations.AlterModelOptions(
            name='hospitalsmodel',
            options={'verbose_name_plural': 'Hospitals Details'},
        ),
    ]
