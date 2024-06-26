# Generated by Django 4.2.13 on 2024-07-01 01:26

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_tag_blog_tag_name_43b6ed_idx_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='blog_tag_name_unique',
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='blog_tag_name_unique'),
        ),
    ]
