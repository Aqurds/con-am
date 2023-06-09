# Generated by Django 2.2.28 on 2022-11-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("strategies", "0002_auto_20220701_0926"),
    ]

    operations = [
        migrations.AddField(
            model_name="strategypage",
            name="header_button_planting",
            field=models.CharField(
                blank=True,
                help_text="Text of the Planting button in the header section",
                max_length=100,
                null=True,
                verbose_name="Planting Header Button Text",
            ),
        ),
        migrations.AddField(
            model_name="strategypage",
            name="header_button_reaching",
            field=models.CharField(
                blank=True,
                help_text="Text of the Reaching button in the header section",
                max_length=100,
                null=True,
                verbose_name="Reaching Header Button Text",
            ),
        ),
        migrations.AddField(
            model_name="strategypage",
            name="header_button_serving",
            field=models.CharField(
                blank=True,
                help_text="Text of the Serving button in the header section",
                max_length=100,
                null=True,
                verbose_name="Serving Header Button Text",
            ),
        ),
        migrations.AddField(
            model_name="strategypage",
            name="header_button_training",
            field=models.CharField(
                blank=True,
                help_text="Text of the Training button in the header section",
                max_length=100,
                null=True,
                verbose_name="Training Header Button Text",
            ),
        ),
    ]
