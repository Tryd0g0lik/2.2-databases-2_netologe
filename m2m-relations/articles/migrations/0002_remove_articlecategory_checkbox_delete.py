# Generated by Django 4.1.2 on 2022-10-10 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecategory',
            name='checkbox_delete',
        ),
    ]
