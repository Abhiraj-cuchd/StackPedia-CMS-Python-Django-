# Generated by Django 4.1.3 on 2022-11-08 14:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackpedia_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
