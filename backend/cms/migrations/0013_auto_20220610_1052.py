# Generated by Django 2.2.28 on 2022-06-10 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prayers', '0002_auto_20220603_0410'),
        ('go', '0001_initial'),
        ('give', '0005_auto_20220609_1459'),
        ('cms', '0012_remove_gregmundisinitiative_initiatives_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='give_page',
            field=models.ForeignKey(blank=True, help_text='Give page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='give.GivePage', verbose_name='Give Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='go_page',
            field=models.ForeignKey(blank=True, help_text='Go page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='go.GoPage', verbose_name='Go Page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='pray_page',
            field=models.ForeignKey(blank=True, help_text='Prayer page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='prayers.PrayerPage', verbose_name='Prayer Page'),
        ),
    ]
