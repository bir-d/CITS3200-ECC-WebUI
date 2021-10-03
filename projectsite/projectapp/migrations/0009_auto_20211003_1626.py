# Generated by Django 3.2.7 on 2021-10-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0008_workstation_workstation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('display_name', models.CharField(max_length=255)),
                ('display_on', models.BooleanField()),
                ('media', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='video_wall_panel',
            name='media',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='video_wall_panel_group',
            name='media',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='workstation',
            name='media',
            field=models.CharField(max_length=255, null=True),
        ),
    ]