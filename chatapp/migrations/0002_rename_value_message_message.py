# Generated by Django 5.0.4 on 2024-04-08 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='value',
            new_name='message',
        ),
    ]
