# Generated by Django 4.1 on 2023-05-16 05:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnonComplaint",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_type", models.CharField(max_length=50)),
                ("complaint_desc", models.TextField(max_length=500)),
                ("complaint_loc", models.CharField(max_length=150)),
                (
                    "complaint_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("complaint_status", models.CharField(max_length=50)),
                (
                    "complaint_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="complaints/images"
                    ),
                ),
                (
                    "complaint_video",
                    models.FileField(
                        blank=True, null=True, upload_to="complaints/videos"
                    ),
                ),
                ("complaint_citizen", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="EmergencyComplaint",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_type", models.CharField(max_length=50)),
                (
                    "complaint_desc",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("complaint_city", models.CharField(max_length=150)),
                ("complaint_loc", models.CharField(max_length=150)),
                (
                    "complaint_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "complaint_status",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "complaint_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="complaints/images"
                    ),
                ),
                (
                    "complaint_video",
                    models.FileField(
                        blank=True, null=True, upload_to="complaints/videos"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NormalComplaint",
            fields=[
                ("complaint_id", models.AutoField(primary_key=True, serialize=False)),
                ("complaint_type", models.CharField(max_length=50)),
                ("complaint_desc", models.TextField(max_length=500)),
                ("complaint_city", models.CharField(max_length=150)),
                ("complaint_loc", models.CharField(max_length=150)),
                (
                    "complaint_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("complaint_status", models.CharField(max_length=50)),
                (
                    "complaint_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="complaints/images"
                    ),
                ),
                (
                    "complaint_doc",
                    models.FileField(blank=True, null=True, upload_to="complaints/doc"),
                ),
                ("complaint_citizen", models.CharField(max_length=50)),
            ],
        ),
    ]
