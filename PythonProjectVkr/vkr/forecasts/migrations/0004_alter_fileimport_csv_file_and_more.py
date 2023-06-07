# Generated by Django 4.2.1 on 2023-05-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forecasts", "0003_fileimport"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fileimport",
            name="csv_file",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="fileimport",
            name="date_added",
            field=models.DateField(auto_now=True),
        ),
    ]
