# Generated by Django 3.0.7 on 2021-02-12 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.IntegerField(primary_key=True, serialize=False)),
                ('album_name', models.CharField(max_length=100)),
                ('album_pic', models.CharField(max_length=250)),
                ('musdir', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=70)),
                ('singer', models.CharField(max_length=150)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
