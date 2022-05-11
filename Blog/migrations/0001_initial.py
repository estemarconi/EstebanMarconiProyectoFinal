# Generated by Django 4.0.3 on 2022-05-06 20:12

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True)),
                ('subtitulo', models.CharField(max_length=200, unique=True)),
                ('url', models.CharField(max_length=200, unique=True)),
                ('imagen', models.ImageField(upload_to='featured_image/%Y/%m/%d/')),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
                ('creado', models.DateField(auto_now_add=True)),
                ('estado', models.IntegerField(choices=[(0, 'Borrador'), (1, 'Publicado')], default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]