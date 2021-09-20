# Generated by Django 3.2.7 on 2021-09-19 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lights_Group',
            fields=[
                ('id', models.PositiveIntegerField(max_length=2, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255)),
                ('colour', models.PositiveIntegerField()),
                ('brightness', models.PositiveIntegerField()),
                ('group_on', models.BooleanField()),
                ('selected', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Video_Wall_Panel_Group',
            fields=[
                ('id', models.PositiveIntegerField(max_length=1, primary_key=True, serialize=False)),
                ('group_on', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Workstations',
            fields=[
                ('id', models.PositiveIntegerField(max_length=1, primary_key=True, serialize=False)),
                ('station_on', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Video_Wall_Panel',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('panel_on', models.BooleanField()),
                ('video_wall_panel_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.video_wall_panel_group')),
            ],
        ),
        migrations.CreateModel(
            name='Lights',
            fields=[
                ('id', models.PositiveIntegerField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('colour', models.PositiveIntegerField()),
                ('brightness', models.PositiveIntegerField()),
                ('light_on', models.BooleanField()),
                ('selected', models.BooleanField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.lights_group')),
            ],
        ),
    ]