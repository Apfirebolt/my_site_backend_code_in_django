# Generated by Django 3.0.5 on 2020-05-28 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_projectimages_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Python', 'Python'), ('Javascript', 'Javascript'), ('React JS', 'React JS'), ('Vue JS', 'Vue JS'), ('Angular', 'Angular'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('Bootstrap', 'Bootstrap'), ('Materialize', 'Materialize'), ('Bulma', 'Bulma'), ('Node', 'Node'), ('Jquery', 'Jquery'), ('Express', 'Express'), ('Nuxt JS', 'Nuxt JS'), ('PHP', 'PHP'), ('Laravel', 'Laravel'), ('Mongo DB', 'Mongo DB'), ('MySQL', 'MySQL')], max_length=200, verbose_name='Technology Name')),
            ],
            options={
                'verbose_name_plural': 'Technology',
            },
        ),
    ]
