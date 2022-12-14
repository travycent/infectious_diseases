# Generated by Django 3.2.10 on 2022-11-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospitals', '0001_initial'),
        ('disease_types', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseReportModel',
            fields=[
                ('diisease_report_id', models.AutoField(primary_key=True, serialize=False)),
                ('death_count', models.IntegerField(blank=True)),
                ('new_case_count', models.IntegerField(blank=True)),
                ('discharge_count', models.IntegerField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('disease_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disease_types.diseasetypesmodel')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospitalsmodel')),
            ],
            options={
                'verbose_name_plural': 'Disease Reports',
            },
        ),
    ]
