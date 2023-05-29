# Generated by Django 2.2.28 on 2022-05-10 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videos", "0003_videopage_is_featured"),
    ]

    operations = [
        migrations.AddField(
            model_name="videopage",
            name="thumbnail_image_alt_text",
            field=models.CharField(
                blank=True,
                help_text="Alt text for the thumbnail image",
                max_length=100,
                null=True,
                verbose_name="Thumbnail Image Alt Text",
            ),
        ),
    ]
