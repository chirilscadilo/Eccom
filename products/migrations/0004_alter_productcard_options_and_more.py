# Generated by Django 4.0.6 on 2022-10-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productcard_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcard',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='productcard',
            name='product_image',
            field=models.ImageField(blank=True, default='default-product.png', null=True, upload_to='card/'),
        ),
    ]
