# Generated by Django 2.2.3 on 2019-09-14 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_courses_name_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses_name',
            old_name='pub_date',
            new_name='pub',
        ),
    ]
