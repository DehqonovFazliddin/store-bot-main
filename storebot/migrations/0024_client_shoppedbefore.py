# Generated by Django 3.1 on 2021-12-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0023_auto_20211225_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='shoppedBefore',
            field=models.BooleanField(default=False, verbose_name='Avval biron narsa harid qilganmi?'),
        ),
    ]
