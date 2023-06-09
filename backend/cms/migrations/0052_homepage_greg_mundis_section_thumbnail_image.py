# Generated by Django 2.2.28 on 2022-12-29 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('cms', '0051_homepage_login_modal_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='greg_mundis_section_thumbnail_image',
            field=models.ForeignKey(blank=True, help_text='Thumbnail image that is going to be displayed for the video in Greg Mundis Section.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
