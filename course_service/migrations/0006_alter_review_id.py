# Generated by Django 4.1 on 2023-03-30 23:28

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course_service', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=6, max_length=6, prefix='', primary_key=True, serialize=False),
        ),
    ]
