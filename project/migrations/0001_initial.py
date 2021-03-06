# Generated by Django 3.0.5 on 2020-05-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250, verbose_name='Project Name')),
                ('project_description', models.TextField(verbose_name='Project Description')),
                ('project_url', models.URLField(verbose_name='Project Url')),
                ('project_technology', models.CharField(max_length=250, verbose_name='Project Technology')),
            ],
            options={
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_image', models.ImageField(upload_to='project_images')),
                ('related_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'verbose_name_plural': 'Project Images',
            },
        ),
    ]
