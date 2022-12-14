# Generated by Django 4.0.6 on 2022-08-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=200)),
                ('from_movie', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='apiapp.singer')),
            ],
        ),
    ]
