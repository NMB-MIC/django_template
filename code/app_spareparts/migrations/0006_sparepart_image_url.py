# Generated by Django 4.0.4 on 2022-05-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0005_rename_stocks_sparepart'),
    ]

    operations = [
        migrations.AddField(
            model_name='sparepart',
            name='image_url',
            field=models.CharField(max_length=50, null=True),
        ),
    ]