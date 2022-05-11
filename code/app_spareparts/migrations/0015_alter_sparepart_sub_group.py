# Generated by Django 4.0.4 on 2022-05-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spareparts', '0014_alter_sparepart_sub_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sparepart',
            name='sub_group',
            field=models.CharField(choices=[('camera', 'camera'), ('robot', 'robot'), ('bearing', 'bearing'), ('controller', 'controller'), ('common', 'common')], max_length=20, null=True),
        ),
    ]