# Generated by Django 4.2 on 2024-08-01 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suco_obulo', '0001_obulo_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('title_en', models.CharField(max_length=50, null=True)),
                ('title_tet', models.CharField(max_length=50, null=True)),
                ('overview', models.TextField()),
                ('overview_en', models.TextField(null=True)),
                ('overview_tet', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='obulo_images/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suco_obulo.page')),
            ],
        ),
    ]
