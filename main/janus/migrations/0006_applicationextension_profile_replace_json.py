# Generated by Django 2.0.7 on 2018-07-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('janus', '0005_applicationextension_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationextension',
            name='profile_replace_json',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]