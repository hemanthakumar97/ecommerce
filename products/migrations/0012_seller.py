# Generated by Django 2.2 on 2020-08-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_laptop_ssd_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=20)),
                ('bsr', models.CharField(max_length=255)),
                ('doa', models.DateField()),
            ],
        ),
    ]
