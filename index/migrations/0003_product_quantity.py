# Generated by Django 4.1.7 on 2023-04-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
