# Generated by Django 2.2.28 on 2022-11-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0036_auto_20221114_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingautomationsystem',
            name='bridge_the_gap_sign_up_subscription',
            field=models.TextField(blank=True, help_text='Set the form in the bridge the gap section in prayers page', null=True, verbose_name='Bridge The Gap Sign Up Subscription Form'),
        ),
        migrations.AddField(
            model_name='marketingautomationsystem',
            name='contact_us',
            field=models.TextField(blank=True, help_text='Set the form in the contact us page', null=True, verbose_name='Contact Us Form'),
        ),
        migrations.AddField(
            model_name='marketingautomationsystem',
            name='media_hub_register',
            field=models.TextField(blank=True, help_text='Set the form for the media hub', null=True, verbose_name='Media Hub Register Form'),
        ),
        migrations.AddField(
            model_name='marketingautomationsystem',
            name='media_hub_support_request',
            field=models.TextField(blank=True, help_text='Set the form for the media hub support', null=True, verbose_name='Media Hub Support Request Form'),
        ),
    ]
