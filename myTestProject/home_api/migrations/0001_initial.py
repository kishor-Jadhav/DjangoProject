# Generated by Django 5.0.3 on 2024-04-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModels',
            fields=[
                ('profile_Id', models.AutoField(primary_key=True, serialize=False)),
                ('name_field', models.TextField()),
                ('age_field', models.IntegerField()),
            ],
        ),
    ]
