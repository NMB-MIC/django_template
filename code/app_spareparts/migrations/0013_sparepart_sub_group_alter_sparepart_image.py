# Generated by Django 4.0.4 on 2022-05-07 13:59

import app_spareparts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0012_alter_sparepart_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='sub_group',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sparepart',
            name='image',
            field=models.ImageField(unique=True, upload_to=app_spareparts.models.user_directory_path),
        ),
    ]
