# Generated by Django 4.2.4 on 2023-08-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0002_category_slug_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name', 'description']},
        ),
    ]
