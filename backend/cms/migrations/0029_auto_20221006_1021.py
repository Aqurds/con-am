# Generated by Django 2.2.28 on 2022-10-06 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0028_marketingautomationsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuexplorepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Image that will be shown for the page in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='menuresourcepage',
            name='external_page_url',
            field=models.TextField(blank=True, help_text='URL of the external page you want to add', null=True, verbose_name='External Page URL'),
        ),
        migrations.AlterField(
            model_name='menuresourcepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Image that will be shown for the page in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='menustrategypage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Image that will be shown for the page in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
