# Generated by Django 2.2.27 on 2022-04-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20220405_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gregmundisinitiative',
            name='message_section',
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='message_body',
            field=models.TextField(blank=True, help_text='Body for the heading of the page', null=True, verbose_name='Message Body'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='message_heading',
            field=models.CharField(blank=True, help_text='Message Heading for the page', max_length=100, null=True, verbose_name='Message Heading'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='message_video_embed_url',
            field=models.CharField(blank=True, help_text='This needs to be the embed URL of the video or else the video player will not work', max_length=100, null=True, verbose_name='Message Video Embed URL'),
        ),
    ]
