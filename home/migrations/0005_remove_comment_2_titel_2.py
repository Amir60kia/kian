# Generated by Django 4.2.6 on 2023-10-23 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_comment_2_titel_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_2',
            name='titel_2',
        ),
    ]
