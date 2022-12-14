# Generated by Django 4.0.2 on 2022-04-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=40)),
                ('releaseYear', models.IntegerField()),
            ],
            options={
                'ordering': ['game'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('buisness', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('machines', models.ManyToManyField(to='main.Machine')),
            ],
            options={
                'ordering': ['zip'],
            },
        ),
    ]
