# Generated by Django 4.1.6 on 2023-03-26 09:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_post_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='c',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
