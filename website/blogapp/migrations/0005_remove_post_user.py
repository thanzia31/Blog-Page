# Generated by Django 4.1.6 on 2023-03-09 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_post_user_alter_post_like_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]