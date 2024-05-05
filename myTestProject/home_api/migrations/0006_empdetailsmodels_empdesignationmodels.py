# Generated by Django 5.0.3 on 2024-04-17 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_api', '0005_authormodels_blogmodels_entrymodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetailsModels',
            fields=[
                ('Emp_Id', models.AutoField(primary_key=True, serialize=False)),
                ('empName', models.TextField()),
                ('empAge', models.IntegerField()),
                ('empSalary', models.IntegerField()),
                ('empShift', models.TextField()),
                ('Comp_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_api.companymodels')),
            ],
        ),
        migrations.CreateModel(
            name='EmpDesignationModels',
            fields=[
                ('des_Id', models.AutoField(primary_key=True, serialize=False)),
                ('desName', models.TextField()),
                ('Emp_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_api.empdetailsmodels')),
            ],
        ),
    ]
