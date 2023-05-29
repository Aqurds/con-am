# Generated by Django 2.2.28 on 2022-05-12 02:52

from django.db import migrations, models
import django.db.models.deletion
import home.utils
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the prayer.', max_length=100, null=True, verbose_name='Name')),
                ('body', models.TextField(blank=True, help_text='Body of the prayer.', null=True, verbose_name='Body')),
                ('image', models.ImageField(blank=True, help_text='Image of the prayer', null=True, upload_to=home.utils.get_upload_path, verbose_name='Image')),
                ('image_alt_text', models.CharField(blank=True, help_text='Alt text for the image of the prayer', max_length=100, null=True, verbose_name='Image Alt Text')),
            ],
            options={
                'verbose_name': 'Prayer',
                'verbose_name_plural': 'Prayers',
            },
        ),
        migrations.CreateModel(
            name='PrayerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header_title', models.CharField(blank=True, help_text='Title for the header portion of the prayer page.', max_length=100, null=True, verbose_name='Header Title')),
                ('header_body', models.TextField(blank=True, help_text='Text in header portion of the prayer page.', null=True, verbose_name='Header Body')),
                ('pray_band_body', wagtail.core.fields.RichTextField(blank=True, help_text='Text in the body of the pray band portion of the prayer page.', null=True, verbose_name='Pray Band Body')),
            ],
            options={
                'verbose_name': 'Prayer Page',
                'verbose_name_plural': 'Prayer Pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SocialPrayerFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the social prayer feed.', max_length=100, null=True, verbose_name='Name')),
                ('body', models.TextField(blank=True, help_text='Body of the social prayer feed.', null=True, verbose_name='Body')),
                ('image', models.ImageField(blank=True, help_text='Image of the social prayer feed', null=True, upload_to=home.utils.get_upload_path, verbose_name='Image')),
                ('image_alt_text', models.CharField(blank=True, help_text='Alt text for the image of the social prayer', max_length=100, null=True, verbose_name='Image Alt Text')),
            ],
            options={
                'verbose_name': 'Social Prayer Feed',
                'verbose_name_plural': 'Social Prayer Feeds',
            },
        ),
    ]
