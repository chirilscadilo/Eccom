# Generated by Django 4.0.6 on 2022-10-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
