# Generated by Django 2.2.28 on 2022-07-01 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('individual_missionaries', '0003_auto_20220616_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualmissionarypage',
            name='missionary',
        ),
        migrations.DeleteModel(
            name='Missionary',
        ),
    ]
