# Generated by Django 2.2.3 on 2019-09-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_java_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses_name',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
