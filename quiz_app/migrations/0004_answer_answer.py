# Generated by Django 2.2.7 on 2020-08-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0003_auto_20200803_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.CharField(default='default', max_length=255),
            preserve_default=False,
        ),
    ]
