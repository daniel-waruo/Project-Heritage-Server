# Generated by Django 2.2.6 on 2019-10-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_group', models.CharField(max_length=30)),
                ('facilitator', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
