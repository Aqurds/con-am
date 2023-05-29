# Generated by Django 2.2.28 on 2022-06-17 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindAMissionaryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('introduction', models.TextField(blank=True, help_text='Text to describe the page', verbose_name='Introduction')),
                ('header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the header image of the page', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('header_image', models.ForeignKey(blank=True, help_text='Header image that is going to be displayed for the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
