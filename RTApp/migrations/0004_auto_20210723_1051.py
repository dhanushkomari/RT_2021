# Generated by Django 3.1.4 on 2021-07-23 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RTApp', '0003_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='detail_id',
            new_name='data_id',
        ),
    ]