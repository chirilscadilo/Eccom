# Generated by Django 4.0.6 on 2022-11-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_remove_orderitem_have_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcard',
            name='has_size',
            field=models.BooleanField(default=True),
        ),
    ]
