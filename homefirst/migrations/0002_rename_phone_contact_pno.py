# Generated by Django 4.2.1 on 2023-05-06 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homefirst', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='pno',
        ),
    ]
