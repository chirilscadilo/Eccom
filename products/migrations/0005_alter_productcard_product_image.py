# Generated by Django 4.0.6 on 2022-11-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productcard_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcard',
            name='product_image',
            field=models.ImageField(blank=True, default='default-product.png', null=True, upload_to='product_images/'),
        ),
    ]
