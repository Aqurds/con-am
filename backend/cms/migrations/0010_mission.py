# Generated by Django 2.2.28 on 2022-06-07 09:44

import json
from pathlib import Path

from django.conf import settings
from django.db import migrations, models
import home.utils


def add_mission_initial_values(apps, schema_editor):
    path = Path(settings.BASE_DIR + "/cms/fixtures/missions.json")

    with path.open() as data_file:
        json_file = json.load(data_file)

    Mission = apps.get_model("cms", "Mission")

    for mission in json_file:
        name = mission.get("fields").get("name")
        Mission.objects.create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ("cms", "0009_auto_20220523_1403"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mission",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Name of the mission",
                        max_length=100,
                        null=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Image of the mission",
                        null=True,
                        upload_to=home.utils.get_upload_path,
                        verbose_name="Image",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Description of the mission",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mission",
                "verbose_name_plural": "Missions",
            },
        ),
        migrations.RunPython(add_mission_initial_values, migrations.RunPython.noop),
    ]
