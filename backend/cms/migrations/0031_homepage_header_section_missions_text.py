# Generated by Django 2.2.28 on 2022-11-09 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0030_auto_20221006_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_section_missions_text',
            field=models.CharField(blank=True, help_text='Set the missions text for the header section', max_length=255, null=True, verbose_name='Header Section Missions Text'),
        ),
    ]
