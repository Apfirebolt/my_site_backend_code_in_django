# Generated by Django 3.0.5 on 2020-05-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamousQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('quoted_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Famous Quotes',
            },
        ),
    ]
