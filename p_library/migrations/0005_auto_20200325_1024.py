# Generated by Django 2.2.6 on 2020-03-25 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200325_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='name',
            new_name='full_name',
        ),
    ]
