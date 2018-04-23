# Generated by Django 2.0.3 on 2018-04-21 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0002_auto_20180421_1659'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('rating', models.IntegerField(default=0)),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lat', models.FloatField(blank=True, default=59.955413)),
                ('lng', models.FloatField(blank=True, default=30.337)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(blank=True, related_name='review_downvotes', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(db_column='location', on_delete=django.db.models.deletion.DO_NOTHING, to='locations.Location')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='tags.Tag')),
                ('upvotes', models.ManyToManyField(blank=True, related_name='review_upvotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
