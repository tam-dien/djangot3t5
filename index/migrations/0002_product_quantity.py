# Generated by Django 4.1.7 on 2023-04-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
