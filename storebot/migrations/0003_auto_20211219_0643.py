# Generated by Django 3.1 on 2021-12-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storebot', '0002_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user_id',
        ),
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='Telegram username'),
        ),
    ]
