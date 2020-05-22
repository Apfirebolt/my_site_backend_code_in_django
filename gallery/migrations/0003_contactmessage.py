# Generated by Django 3.0.5 on 2020-05-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200519_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
                ('website', models.URLField(verbose_name='Website URL')),
            ],
            options={
                'verbose_name_plural': 'Contact Message',
            },
        ),
    ]
