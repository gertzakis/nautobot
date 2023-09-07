# Generated by Django 3.2.18 on 2023-06-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0047_status_nonnullable"),
        ("virtualization", "0025_status_nonnullable"),
        ("ipam", "0035_ensure_all_services_fit_uniqueness_constraint"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="service",
            constraint=models.UniqueConstraint(fields=("name", "device"), name="unique_device_service_name"),
        ),
        migrations.AddConstraint(
            model_name="service",
            constraint=models.UniqueConstraint(
                fields=("name", "virtual_machine"), name="unique_virtual_machine_service_name"
            ),
        ),
    ]