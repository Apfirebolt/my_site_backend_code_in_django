# Generated by Django 3.0.5 on 2020-05-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimages',
            name='image_description',
            field=models.CharField(default='No description available', max_length=250, verbose_name='Image Description'),
        ),
    ]
