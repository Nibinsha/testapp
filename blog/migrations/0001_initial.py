# Generated by Django 2.0 on 2019-08-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('contactNo', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=60)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
