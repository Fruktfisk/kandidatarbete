# Generated by Django 2.0.3 on 2018-04-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20180408_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.CharField(max_length=120),
        ),
    ]
