# Generated by Django 4.2.1 on 2023-05-07 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homefirst', '0002_rename_phone_contact_pno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]