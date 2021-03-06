# Generated by Django 2.2 on 2020-08-01 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200801_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectronicComponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_1',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_2',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_3',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_4',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_5',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_6',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_7',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='pro_banner_8',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='producs/'),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_details_electronics',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ElectronicComponents'),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_details_laptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Laptop'),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_details_mobile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Mobile'),
        ),
        migrations.AddField(
            model_name='product',
            name='technical_details_sensors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Sensors'),
        ),
    ]
