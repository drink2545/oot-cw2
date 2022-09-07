# Generated by Django 4.1.1 on 2022-09-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="stock_item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=255)),
                ("item_type", models.CharField(max_length=255)),
                ("cat", models.CharField(max_length=255)),
                ("brand_name", models.CharField(max_length=255)),
                ("qty", models.IntegerField()),
                ("price", models.IntegerField()),
            ],
        ),
    ]
