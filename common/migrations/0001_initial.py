# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
                ('iframe_data', models.TextField(max_length=500)),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('audios', models.ManyToManyField(to='common.Audio')),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
                ('file', sorl.thumbnail.fields.ImageField(upload_to='image/%Y/%m/%d')),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.CommonMedia')),
                ('iframe_data', models.TextField(max_length=500)),
            ],
            bases=('common.commonmedia',),
        ),
        migrations.AddField(
            model_name='gallery',
            name='images',
            field=models.ManyToManyField(to='common.Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.ManyToManyField(to='common.Gallery'),
        ),
        migrations.AddField(
            model_name='event',
            name='texts',
            field=models.ManyToManyField(to='common.Article'),
        ),
        migrations.AddField(
            model_name='event',
            name='videos',
            field=models.ManyToManyField(to='common.Video'),
        ),
    ]
