# Generated by Django 4.2.1 on 2023-05-06 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Models",
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
                ("title", models.CharField(max_length=50, verbose_name="Название")),
                ("anons", models.CharField(max_length=250, verbose_name="Анонс")),
                ("full_text", models.TextField(verbose_name="Статья")),
                ("date", models.DateTimeField(verbose_name="Дата публикации")),
                ("time", models.DateTimeField(verbose_name="Время публикации")),
            ],
            options={
                "verbose_name": "Прогноз",
                "verbose_name_plural": "Прогнозы",
            },
        ),
    ]
