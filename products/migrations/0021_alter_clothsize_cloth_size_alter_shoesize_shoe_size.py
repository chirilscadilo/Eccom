# Generated by Django 4.1.4 on 2023-02-13 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_remove_orderitem_cloth_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothsize',
            name='cloth_size',
            field=models.CharField(blank=True, default='S', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='shoesize',
            name='shoe_size',
            field=models.FloatField(blank=True, default=36.0, null=True),
        ),
    ]