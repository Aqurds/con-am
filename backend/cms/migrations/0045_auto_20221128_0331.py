# Generated by Django 2.2.28 on 2022-11-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0044_auto_20221125_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='executive_priorities_title',
            field=models.CharField(blank=True, help_text='Set text for the Executive Priorities Title', max_length=100, null=True, verbose_name='Executive Priorities Title'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='executive_read_all_button',
            field=models.CharField(blank=True, help_text='Set text for the Read All button', max_length=100, null=True, verbose_name='Read All Button Text'),
        ),
    ]
