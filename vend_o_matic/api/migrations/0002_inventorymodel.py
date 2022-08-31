# Generated by Django 4.1 on 2022-08-31 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="InventoryModel",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BB", "Butterbeer"),
                            ("ED", "Ent Draught"),
                            ("AB", "Ambrosia"),
                        ],
                        max_length=15,
                    ),
                ),
                ("quantity", models.IntegerField()),
            ],
        ),
    ]
