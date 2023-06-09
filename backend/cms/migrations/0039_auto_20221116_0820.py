# Generated by Django 2.2.28 on 2022-11-16 08:20

from django.db import migrations, models
import django.db.models.deletion
import home.utils
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('cms', '0038_footersection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footersection',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='are_you_called_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='connect_section_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='connect_section_get_in_touch_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='copyright_text',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_africa_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_asia_pacific_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_eurasia_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_europe_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_international_ministries_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_latin_america_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='explore_section_northern_asia_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_about_us_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_executive_office_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_give_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_go_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_prayer_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='home_section_privacy_permissions_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_merchandise_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_photos_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_stories_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_videos_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='resources_section_world_view_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='strategy_section_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='strategy_section_planting_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='strategy_section_reaching_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='strategy_section_serving_button',
        ),
        migrations.RemoveField(
            model_name='footersection',
            name='strategy_section_training_button',
        ),
        migrations.CreateModel(
            name='FooterStrategyColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Set the name of the field to be shown in the strategy section', max_length=100, null=True, verbose_name='Name')),
                ('is_top_link', models.BooleanField(default=False, help_text='Check the box to set this to True and make text bold and moved at the top of the column', null=True, verbose_name='Is Top text')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add Strategy column buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_strategy', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer Fifth Column',
                'verbose_name_plural': 'Footer Fifth Column',
            },
        ),
        migrations.CreateModel(
            name='FooterResourcesColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Set the name of the field to be shown in the resources section', max_length=100, null=True, verbose_name='Name')),
                ('is_top_link', models.BooleanField(default=False, help_text='Check the box to set this to True and make text bold and moved at the top of the column', null=True, verbose_name='Is Top text')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add Resources column buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_resources', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer Third Column',
                'verbose_name_plural': 'Footer Third Column',
            },
        ),
        migrations.CreateModel(
            name='FooterInformationColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.FileField(blank=True, help_text='Logo that will be shown in the first section of the footer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Header Image')),
                ('header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the header image', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('button_name', models.CharField(blank=True, help_text='Set the name of the button to be shown in the first section', max_length=100, null=True, verbose_name=' Button Name')),
                ('address1', models.CharField(blank=True, help_text='Address 1 text in the footer section', max_length=255, null=True, verbose_name='Address 1')),
                ('address2', models.CharField(blank=True, help_text='Address 2 text in the footer section', max_length=255, null=True, verbose_name='Address 2')),
                ('phone_number', models.CharField(blank=True, help_text='Phone number in the footer section', max_length=255, null=True, verbose_name='Phone Number')),
                ('copyright_text', models.CharField(blank=True, help_text='Copyright text in the footer section', max_length=255, null=True, verbose_name='Copyright text')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add first section column text/buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_information', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer First Column',
                'verbose_name_plural': 'Footer First Column',
            },
        ),
        migrations.CreateModel(
            name='FooterHomeColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Set the name of the field to be shown in the home section', max_length=100, null=True, verbose_name='Name')),
                ('is_top_link', models.BooleanField(default=False, help_text='Check the box to set this to True and make text bold and moved at the top of the column', null=True, verbose_name='Is Top text')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add Home column buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_home', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer Second Column',
                'verbose_name_plural': 'Footer Second Column',
            },
        ),
        migrations.CreateModel(
            name='FooterExploreColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Set the name of the field to be shown in the explore section', max_length=100, null=True, verbose_name='Name')),
                ('is_top_link', models.BooleanField(default=False, help_text='Check the box to set this to True and make text bold and moved at the top of the column', null=True, verbose_name='Is Top text')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add Explore column buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_explore', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer Fourth Column',
                'verbose_name_plural': 'Footer Fourth Column',
            },
        ),
        migrations.CreateModel(
            name='FooterConnectColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(blank=True, help_text='Set the top name to be shown in the sixth section', max_length=100, null=True, verbose_name='Name')),
                ('button_name', models.CharField(blank=True, help_text='Set the name of the button to be shown in the sixth section', max_length=100, null=True, verbose_name='Button Name')),
                ('facebook_header_image', models.FileField(blank=True, help_text='Facebook logo that will be shown in the sixth section of the footer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Facebook Header Image')),
                ('facebook_header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the facebook header image', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('facebook_url', models.CharField(blank=True, help_text='Facebook URL link', max_length=255, null=True, verbose_name='Facebook URL')),
                ('vimeo_header_image', models.FileField(blank=True, help_text='Vimeo logo that will be shown in the sixth section of the footer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Vimeo Header Image')),
                ('vimeo_header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Vimeo header image', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('vimeo_url', models.CharField(blank=True, help_text='Viemo URL link', max_length=255, null=True, verbose_name='Vimeo URL')),
                ('youtube_header_image', models.FileField(blank=True, help_text='Youtube logo that will be shown in the sixth section of the footer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Youtube Header Image')),
                ('youtube_header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the youtube header image', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('youtube_url', models.CharField(blank=True, help_text='Youtube URL link', max_length=255, null=True, verbose_name='Youtube URL')),
                ('instagram_header_image', models.FileField(blank=True, help_text='Instagram logo that will be shown in the sixth section of the footer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Instagram Header Image')),
                ('instagram_header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the Instagram header image', max_length=255, null=True, verbose_name='Instagram Header Image Alt Text')),
                ('instagram_url', models.CharField(blank=True, help_text='Instagram URL link', max_length=255, null=True, verbose_name='Instagram URL')),
                ('footer_column', modelcluster.fields.ParentalKey(blank=True, help_text='Add Connect column buttons here', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='footer_column_connect', to='cms.FooterSection')),
                ('page', models.ForeignKey(blank=True, help_text='Set the page that you want to link the field to', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Footer Sixth Column',
                'verbose_name_plural': 'Footer Sixth Column',
            },
        ),
    ]
