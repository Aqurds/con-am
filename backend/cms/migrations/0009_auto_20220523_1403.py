# Generated by Django 2.2.28 on 2022-05-23 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('cms', '0008_auto_20220516_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='prayer_section',
        ),
        migrations.AddField(
            model_name='homepage',
            name='prayer_body',
            field=models.TextField(blank=True, help_text='Body of the prayer that will be shown in the prayer section', null=True, verbose_name='Prayer Body'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='prayer_image',
            field=models.ForeignKey(blank=True, help_text='Image that will be shown for the prayer section in the home page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Prayer Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='prayer_image_alt_text',
            field=models.CharField(blank=True, help_text='Alt text for the image that will be shwon for the prayer section in the home page', max_length=255, null=True, verbose_name='Prayer Image Alt Text'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='prayer_title',
            field=models.CharField(blank=True, help_text='Title of the prayer that will be shown in the prayer section', max_length=255, null=True, verbose_name='Prayer Title'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='show_prayer_section',
            field=models.BooleanField(default=True, help_text='Determines whether the prayer section will be shown in the home page', verbose_name='Show Prayer Section'),
        ),
    ]
