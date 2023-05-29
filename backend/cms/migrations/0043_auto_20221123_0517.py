# Generated by Django 2.2.28 on 2022-11-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0042_auto_20221118_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='greg_mundis_section_bottom_text',
            field=models.CharField(blank=True, help_text='Set the bottom text for the Greg Mundis section in the home page', max_length=200, null=True, verbose_name='Greg Mundis Section Bottom Text'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='greg_mundis_section_top_text',
            field=models.CharField(blank=True, help_text='Set the top text for the Greg Mundis section in the home page', max_length=200, null=True, verbose_name='Greg Mundis Section Top Text'),
        ),
    ]
