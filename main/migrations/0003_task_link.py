# Generated by Django 3.1 on 2020-08-20 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200819_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000, verbose_name='Силка'),
            preserve_default=False,
        ),
    ]
