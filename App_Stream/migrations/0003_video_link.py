# Generated by Django 3.2.6 on 2021-11-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Stream', '0002_rename_title_category_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
