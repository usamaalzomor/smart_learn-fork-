# Generated by Django 4.1 on 2023-03-31 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0006_alter_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]
