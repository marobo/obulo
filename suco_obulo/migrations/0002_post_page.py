# Generated by Django 4.2 on 2024-07-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suco_obulo', '0001_obulo_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Page',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='page',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/obulo_images'),
        ),
    ]
