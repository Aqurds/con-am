# Generated by Django 2.2.28 on 2022-11-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0003_regionpage_region_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionpage',
            name='header_join_the_team_button_url',
            field=models.CharField(blank=True, help_text='Set the URL for Join the team button', max_length=100, null=True, verbose_name='Join the team button url'),
        ),
    ]
