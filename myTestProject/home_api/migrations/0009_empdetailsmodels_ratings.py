# Generated by Django 5.0.3 on 2024-04-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_api', '0008_empdetailsmodels_emphoby'),
    ]

    operations = [
        migrations.AddField(
            model_name='empdetailsmodels',
            name='ratings',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]