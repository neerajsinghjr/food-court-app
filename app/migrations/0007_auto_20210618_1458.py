# Generated by Django 3.0.6 on 2021-06-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210618_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='prid1',
            new_name='pincode',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='prid2',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='prid3',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='qty1',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='qty2',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='qty3',
        ),
        migrations.AddField(
            model_name='orders',
            name='addr',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='phno',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]