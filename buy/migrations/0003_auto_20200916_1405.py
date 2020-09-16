# Generated by Django 2.2 on 2020-09-16 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20200916_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]