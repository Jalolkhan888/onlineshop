# Generated by Django 4.1.5 on 2023-01-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
