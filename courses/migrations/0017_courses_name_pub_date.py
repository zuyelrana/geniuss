# Generated by Django 2.2.3 on 2019-09-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20190910_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses_name',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]