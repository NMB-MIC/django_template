# Generated by Django 4.0.4 on 2022-05-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0002_stocks_name3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='name3',
            new_name='part_number',
        ),
        migrations.RemoveField(
            model_name='stocks',
            name='name2',
        ),
    ]