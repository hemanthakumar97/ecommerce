# Generated by Django 2.2 on 2020-10-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0005_auto_20201010_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
    ]