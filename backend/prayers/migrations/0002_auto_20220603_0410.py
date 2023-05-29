# Generated by Django 2.2.28 on 2022-06-03 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('prayers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayerpage',
            name='header_image',
            field=models.ForeignKey(blank=True, help_text='Header image that is going to be displayed for the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='prayerpage',
            name='header_image_alt_text',
            field=models.CharField(blank=True, help_text='Alt text for the header image of the page', max_length=255, null=True, verbose_name='Header Image Alt Text'),
        ),
    ]
