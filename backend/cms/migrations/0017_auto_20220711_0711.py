# Generated by Django 2.2.28 on 2022-07-11 07:11

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('cms', '0016_missiontext'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactperson',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='contactperson',
            name='page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_persons', to='cms.GregMundisInitiative'),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_address1',
            field=models.CharField(blank=True, help_text='First line of the company address to be displayed in the page', max_length=50, null=True, verbose_name='Address 1'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_address2',
            field=models.CharField(blank=True, help_text='Second line of the company address to be displayed in the page', max_length=50, null=True, verbose_name='Address 2'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_background_image',
            field=models.ForeignKey(blank=True, help_text='Background image of the contact information ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_background_image_alt_text',
            field=models.CharField(blank=True, help_text='Alt text for the background image of the contact information', max_length=100, null=True, verbose_name='Background Image Alt Text'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_company_name',
            field=models.CharField(blank=True, help_text='Company name to be displayed in the page', max_length=50, null=True, verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='gregmundisinitiative',
            name='contact_info_phone_number',
            field=models.CharField(blank=True, help_text='Phone number to be displayed in the page', max_length=50, null=True, verbose_name='Phone Number'),
        ),
        migrations.DeleteModel(
            name='ContactInformation',
        ),
    ]
