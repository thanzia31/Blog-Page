# Generated by Django 4.1.6 on 2023-03-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_field',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]