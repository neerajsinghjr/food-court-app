# Generated by Django 3.0.6 on 2021-06-18 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210618_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdb',
            old_name='msg',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactdb',
            old_name='phno',
            new_name='pno',
        ),
    ]
