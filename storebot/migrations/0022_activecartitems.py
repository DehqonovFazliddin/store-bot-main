# Generated by Django 3.1 on 2021-12-25 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0021_auto_20211223_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveCartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('cart_id', models.IntegerField()),
                ('quantity', models.IntegerField(verbose_name='Miqdori')),
                ('item_code', models.CharField(max_length=36, verbose_name='buyurtma kodi')),
            ],
        ),
    ]