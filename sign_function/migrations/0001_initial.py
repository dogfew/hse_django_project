# Generated by Django 4.1.9 on 2023-06-07 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sign",
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
                    "condition",
                    models.CharField(blank=True, default="Дано число", max_length=128),
                ),
                ("number", models.FloatField(verbose_name="Float Number")),
                ("sign", models.IntegerField()),
                ("sign_text", models.CharField(max_length=16)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
