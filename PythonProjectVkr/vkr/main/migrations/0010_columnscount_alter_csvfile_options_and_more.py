# Generated by Django 4.2.1 on 2023-05-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_fieldname"),
    ]

    operations = [
        migrations.CreateModel(
            name="ColumnsCount",
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
                ("count", models.CharField()),
            ],
            options={
                "verbose_name": "Количество столбцов",
                "verbose_name_plural": "Количество столбцов",
            },
        ),
        migrations.AlterModelOptions(
            name="csvfile",
            options={"verbose_name": "Csv файл", "verbose_name_plural": "Csv файлы"},
        ),
        migrations.AlterModelOptions(
            name="fieldname",
            options={
                "verbose_name": "Прогнозируемое поле",
                "verbose_name_plural": "Прогнозируемые поля",
            },
        ),
    ]
