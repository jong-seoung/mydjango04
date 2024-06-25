# Generated by Django 4.2.13 on 2024-06-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='tag',
            index=models.Index(fields=['name'], name='blog_tag_name_43b6ed_idx'),
        ),
    ]
