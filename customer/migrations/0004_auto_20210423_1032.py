# Generated by Django 3.1.7 on 2021-04-23 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210423_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='state',
            field=models.CharField(max_length=15),
        ),
    ]
