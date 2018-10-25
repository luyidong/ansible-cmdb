# Generated by Django 2.0.1 on 2018-10-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_auto_20180727_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host_release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.TextField()),
                ('release_type', models.CharField(max_length=10)),
                ('release_status', models.BooleanField()),
                ('release_cmd', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]