# Generated by Django 3.0.5 on 2020-05-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_service_respect_dnt"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="collect_ips",
            field=models.BooleanField(default=True),
        ),
    ]