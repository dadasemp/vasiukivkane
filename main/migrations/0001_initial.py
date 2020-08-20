# Generated by Django 3.1 on 2020-08-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
                ('link', models.CharField(max_length=1000, verbose_name='Силка')),
                ('linktext', models.CharField(max_length=40, verbose_name='Текст силки')),
                ('img', models.CharField(max_length=1000, verbose_name='Зображення')),
            ],
        ),
    ]
