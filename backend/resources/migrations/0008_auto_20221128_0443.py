# Generated by Django 2.2.28 on 2022-11-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0007_featuredresourcecenterproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcespage',
            name='photos_card_text',
            field=models.CharField(blank=True, help_text='Set the text for the Photos Card', max_length=255, null=True, verbose_name='Photos Card Text'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='resource_center_go_to_shop_button',
            field=models.CharField(blank=True, help_text='Set the text for the Go to Shop Button', max_length=255, null=True, verbose_name='Resource Center Go To Shop Button Text'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='resource_center_header_title',
            field=models.CharField(blank=True, help_text='Set the text for the Resource Center Header Title', max_length=255, null=True, verbose_name='Resource Center Header Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='resource_center_sub_title',
            field=models.CharField(blank=True, help_text='Set the text for the Resource Center Header Title', max_length=255, null=True, verbose_name='Resource Center Sub Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='stories_card_text',
            field=models.CharField(blank=True, help_text='Set the text for the Stories Card', max_length=255, null=True, verbose_name='Stories Card Text'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='videos_card_text',
            field=models.CharField(blank=True, help_text='Set the text for the Videos Card', max_length=255, null=True, verbose_name='Videos Card Text'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='vital_stats_header_title',
            field=models.CharField(blank=True, help_text='Set the text for the Vital Stats Header Title', max_length=255, null=True, verbose_name='Vital Stats Header Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='vital_stats_sub_title',
            field=models.CharField(blank=True, help_text='Set the text for the Vital Stats Sub Title', max_length=255, null=True, verbose_name='Vital Stats Sub Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='vital_stats_view_button',
            field=models.CharField(blank=True, help_text='Set the text for the Vital Stats View Button', max_length=255, null=True, verbose_name='Vital Stats View Button'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='world_view_section_sub_title',
            field=models.TextField(blank=True, help_text='Set the text for the World View Section Sub Title', null=True, verbose_name='World View Section Sub Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='world_view_section_title',
            field=models.CharField(blank=True, help_text='Set the text for the World View Section Title', max_length=255, null=True, verbose_name='World View Section Title'),
        ),
        migrations.AddField(
            model_name='resourcespage',
            name='world_view_view_all_button',
            field=models.CharField(blank=True, help_text='Set the text for the World View View All Button', max_length=255, null=True, verbose_name='World View View All Button'),
        ),
    ]
