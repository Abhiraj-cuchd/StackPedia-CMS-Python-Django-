# Generated by Django 4.1.3 on 2022-11-30 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stackpedia_app', '0007_blogcomments_delete_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComments',
        ),
    ]