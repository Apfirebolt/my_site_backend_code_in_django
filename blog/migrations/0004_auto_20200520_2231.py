# Generated by Django 3.0.5 on 2020-05-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_uncategorizedblog_unclassifiedblogimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='uncategorizedblog',
            name='blog_slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uncategorizedblog',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='unclassifiedblogimages',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]