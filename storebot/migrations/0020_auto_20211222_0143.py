# Generated by Django 3.1 on 2021-12-22 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0019_auto_20211222_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='buy_all_items',
            field=models.BooleanField(default=False, verbose_name='Barcha narsani sotib oladimi?'),
        ),
        migrations.DeleteModel(
            name='BuyAllItems',
        ),
    ]
