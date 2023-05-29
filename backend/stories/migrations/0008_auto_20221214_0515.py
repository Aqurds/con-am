# Generated by Django 2.2.28 on 2022-12-14 05:15

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20221213_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storypage',
            name='simple_prayer',
        ),
        migrations.RemoveField(
            model_name='storypage',
            name='simple_prayer_header',
        ),
        migrations.AddField(
            model_name='storyindexpage',
            name='simple_prayer',
            field=wagtail.core.fields.RichTextField(blank=True, help_text="Prayer that will be displayed under the 'Todays simple prayer'", null=True, verbose_name='Simple Prayer'),
        ),
        migrations.AddField(
            model_name='storyindexpage',
            name='simple_prayer_header',
            field=models.CharField(blank=True, help_text='Header text in the todays simple prayer section', max_length=255, null=True, verbose_name='Simple Prayer Header'),
        ),
    ]
