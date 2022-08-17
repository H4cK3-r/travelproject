# Generated by Django 4.0.6 on 2022-07-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_desc_people_pepdesc_rename_img_people_pepimg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]
