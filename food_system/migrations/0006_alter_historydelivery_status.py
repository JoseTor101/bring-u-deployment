# Generated by Django 4.2.4 on 2023-12-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_system', '0005_historydelivery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historydelivery',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
