# Generated by Django 2.2.28 on 2022-11-11 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('cms', '0033_homepagemissiontextrotate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header_image_alt_text', models.CharField(blank=True, help_text='Alt text for the header image of the page', max_length=255, null=True, verbose_name='Header Image Alt Text')),
                ('header_form_text', models.CharField(blank=True, help_text='Set the header for the contact form', max_length=255, null=True, verbose_name='Header Form Text')),
                ('location_header_text', models.CharField(blank=True, help_text='Set the location header text', max_length=255, null=True, verbose_name='Location Header Text')),
                ('location_sub_text', models.CharField(blank=True, help_text='Set the location sub text', max_length=255, null=True, verbose_name='Location Sub Text')),
                ('contact_us_address_text1', models.CharField(blank=True, help_text='Set the address text', max_length=255, null=True, verbose_name='Address Text 1')),
                ('contact_us_address_text2', models.CharField(blank=True, help_text='Set the address text', max_length=255, null=True, verbose_name='Address Text 2')),
                ('contact_us_phone_number', models.CharField(blank=True, help_text='Set the phone number', max_length=255, null=True, verbose_name='Phone Number')),
                ('header_image', models.ForeignKey(blank=True, help_text='Header image that is going to be displayed for the page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
            bases=('wagtailcore.page',),
        ),
    ]
