# Generated by Django 3.0.7 on 2021-03-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handlerequests', '0004_webcamimagehandler'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsingMobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('mobile', models.BooleanField(default=True)),
            ],
        ),
    ]
