# Generated by Django 3.0.7 on 2020-06-04 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv_file',
            field=models.FileField(blank=True, null=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
