# Generated by Django 2.2.27 on 2022-03-30 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0062_comment_models_and_pagesubscription"),
        ("cms", "0002_contactinformation_contactperson_gregmundisinitiative"),
    ]

    operations = [
        migrations.AddField(
            model_name="gregmundisinitiative",
            name="initiatives_section",
            field=models.ForeignKey(
                blank=True,
                help_text="Executive Giving Initiatives section of the page",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
                verbose_name="Initiatives Section",
            ),
        ),
    ]
