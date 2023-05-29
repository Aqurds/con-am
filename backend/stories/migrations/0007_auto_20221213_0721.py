# Generated by Django 2.2.28 on 2022-12-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_storysliderheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyindexpage',
            name='giving_initiative_button_text',
            field=models.CharField(blank=True, help_text='Button text in the giving initiave section.', max_length=255, null=True, verbose_name='Giving Initiative Button Text'),
        ),
        migrations.AddField(
            model_name='storyindexpage',
            name='giving_initiative_content',
            field=models.TextField(blank=True, help_text='Giving initiative content shown under the header.', max_length=255, null=True, verbose_name='Giving Initiative Content'),
        ),
        migrations.AddField(
            model_name='storyindexpage',
            name='giving_initiative_header',
            field=models.CharField(blank=True, help_text='Header text shown in giving initiative section.', max_length=255, null=True, verbose_name='Giving Initiative Header'),
        ),
        migrations.AddField(
            model_name='storyindexpage',
            name='story_page_explore_button_text',
            field=models.CharField(blank=True, help_text='Explore button text at the end of every displayed story page.', max_length=255, null=True, verbose_name='Story Page Explore Button Text'),
        ),
        migrations.AddField(
            model_name='storypage',
            name='simple_prayer_header',
            field=models.CharField(blank=True, help_text='Header text in the todays simple prayer section', max_length=255, null=True, verbose_name='Simple Prayer Header'),
        ),
    ]
