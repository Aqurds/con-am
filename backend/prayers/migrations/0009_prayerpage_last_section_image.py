# Generated by Django 2.2.28 on 2022-12-02 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('prayers', '0008_auto_20221125_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='prayerpage',
            name='last_section_image',
            field=models.ForeignKey(blank=True, help_text='Image that is going to be displayed in the bottom section of the page.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
