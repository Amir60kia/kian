# Generated by Django 4.2.6 on 2023-10-23 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_post_5_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_5',
            old_name='image',
            new_name='image_5',
        ),
    ]