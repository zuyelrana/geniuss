# Generated by Django 2.2.3 on 2019-09-14 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_courses_name_pub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses_name',
            name='pub',
        ),
    ]