# Generated by Django 2.2.28 on 2022-11-11 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_contactuspage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_us_first_name', models.CharField(blank=True, help_text='First Name of the contact person', max_length=255, null=True, verbose_name='First Name')),
                ('contact_us_last_name', models.CharField(blank=True, help_text='Last Name of the contact person', max_length=255, null=True, verbose_name='Last Name')),
                ('contact_us_email', models.EmailField(blank=True, help_text='Email address of the contact person', max_length=254, verbose_name='Email Address')),
                ('contact_us_phone_number', models.CharField(blank=True, help_text='Phone number of the contact person', max_length=255, null=True, verbose_name='Phone Number')),
                ('contact_us_church_name', models.CharField(blank=True, help_text='Church name of the contact person', max_length=255, null=True, verbose_name='Church Name')),
                ('contact_us_comment_and_message', models.TextField(blank=True, help_text='Comment and message of the contact person', null=True, verbose_name='Comment and Message')),
            ],
            options={
                'verbose_name': 'Contact Us Form',
                'verbose_name_plural': 'Contact Us Forms',
            },
        ),
    ]
