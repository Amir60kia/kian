# Generated by Django 4.2.6 on 2023-10-23 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_comment_2_titel_2_alter_comment_1_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_2',
            name='titel_2',
            field=models.CharField(max_length=50),
        ),
    ]
