# Generated by Django 3.1 on 2021-12-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True, verbose_name='callback_data'),
        ),
    ]