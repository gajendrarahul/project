# Generated by Django 3.0.5 on 2020-09-12 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='bike_no',
            field=models.CharField(max_length=50),
        ),
    ]
