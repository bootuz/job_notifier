# Generated by Django 3.0.2 on 2020-01-17 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('salary', models.CharField(blank=True, max_length=250)),
                ('company_name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
