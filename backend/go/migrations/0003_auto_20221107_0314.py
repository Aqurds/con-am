# Generated by Django 2.2.28 on 2022-11-07 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('go', '0002_auto_20220627_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='gopage',
            name='header_section_thumbnail',
            field=models.ForeignKey(blank=True, help_text='This serves as the thumbnail of the header section video', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='gopage',
            name='header_section_thumbnail_alt_text',
            field=models.CharField(blank=True, help_text='Alt text for the thumbnail', max_length=255, null=True, verbose_name='Thumbnail Alt Text'),
        ),
        migrations.AddField(
            model_name='gopage',
            name='header_section_video_url',
            field=models.TextField(blank=True, help_text='URL of the video to be shown in the header section. This needs to be the EMBED url of the video or else it will not work properly', null=True, verbose_name='Video URL'),
        ),
    ]
