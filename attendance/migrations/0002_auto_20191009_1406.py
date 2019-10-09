# Generated by Django 2.2.6 on 2019-10-09 14:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20191008_0904'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phClass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.PhClass'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='isPresent',
            field=models.BooleanField(default=False),
        ),
    ]