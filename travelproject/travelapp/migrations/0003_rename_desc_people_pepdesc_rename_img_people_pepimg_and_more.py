# Generated by Django 4.0.6 on 2022-07-28 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc',
            new_name='pepdesc',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='pepimg',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='pepname',
        ),
    ]
