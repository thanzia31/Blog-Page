# Generated by Django 4.1.6 on 2023-03-09 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_post_userlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='userlikes',
        ),
    ]
