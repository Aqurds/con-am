# Generated by Django 2.2.28 on 2022-07-06 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_menuexplorepage_menuresourcepage_menustrategypage'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuexplorepage',
            name='page_title',
            field=models.CharField(blank=True, help_text='Name of the page that will be displayed if you dont want the page name to display in the menu.', max_length=255, null=True, verbose_name='Page Title'),
        ),
        migrations.AddField(
            model_name='menuresourcepage',
            name='external_page_url',
            field=models.TextField(help_text='URL of the external page you want to add', null=True, verbose_name='External Page URL'),
        ),
        migrations.AddField(
            model_name='menuresourcepage',
            name='is_external_page',
            field=models.BooleanField(default=False, help_text='Set this as true if the page youu want to add in the resource section is an external website/page', null=True, verbose_name='Is External Page'),
        ),
        migrations.AddField(
            model_name='menuresourcepage',
            name='page_title',
            field=models.CharField(blank=True, help_text='Name of the page that will be displayed if you dont want the page name to display in the menu.', max_length=255, null=True, verbose_name='Page Title'),
        ),
        migrations.AddField(
            model_name='menustrategypage',
            name='page_section_link',
            field=models.CharField(blank=True, help_text='name of the section you want to go to in the strategy page', max_length=255, null=True, verbose_name='Page Section Link'),
        ),
        migrations.AlterField(
            model_name='menuexplorepage',
            name='page',
            field=models.ForeignKey(blank=True, help_text='Page that you want to show in the explore tab in the menu. This will also serve as the default page title that will be shown in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='menuresourcepage',
            name='page',
            field=models.ForeignKey(blank=True, help_text='Page that you want to show in the resources tab in the menu. This will also serve as the default page title that will be shown in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AlterField(
            model_name='menustrategypage',
            name='page',
            field=models.ForeignKey(blank=True, help_text='Page that you want to show in the strategy tab in the menu. This will also serve as the default page title that will be shown in the menu', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
