# Generated by Django 3.0.5 on 2020-05-19 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('NATURE', 'Nature'), ('COLLEGE', 'College Life'), ('PERSONAL', 'Personal Life'), ('PROGRAMMING', 'Programming'), ('GAMES', 'Games'), ('PHOTOSHOP', 'Photoshop'), ('OTHERS', 'Others')], max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('gallery_image', models.ImageField(upload_to='gallery')),
                ('likes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gallery.Category')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
    ]