# Generated by Django 3.1 on 2021-12-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0020_auto_20211222_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Narxi'),
        ),
    ]
