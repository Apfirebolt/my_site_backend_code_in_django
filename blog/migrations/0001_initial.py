# Generated by Django 3.0.5 on 2020-05-19 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('number_of_blogs', models.IntegerField(default=0, verbose_name='Number of Blogs')),
                ('category_image', models.FileField(blank=True, null=True, upload_to='blog_category_images')),
            ],
            options={
                'verbose_name_plural': 'Category Name',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Blog Title')),
                ('content', models.TextField(verbose_name='Blog Content')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='blog.BlogCategory')),
            ],
            options={
                'verbose_name_plural': 'Blog Post',
            },
        ),
        migrations.CreateModel(
            name='BlogPostImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.FileField(upload_to='blog_images', verbose_name='Blog Image')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Created At')),
                ('image_description', models.TextField(blank=True, default='No description available', null=True, verbose_name='Image Description')),
                ('blog_related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_blog_post', to='blog.BlogPost')),
            ],
            options={
                'verbose_name_plural': 'Blog Images',
            },
        ),
    ]
