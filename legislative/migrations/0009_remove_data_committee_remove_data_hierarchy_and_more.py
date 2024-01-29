# Generated by Django 4.1.12 on 2024-01-25 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0008_data_hierarchy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='committee',
        ),
        migrations.RemoveField(
            model_name='data',
            name='hierarchy',
        ),
        migrations.RemoveField(
            model_name='data',
            name='subcommittee',
        ),
        migrations.RemoveField(
            model_name='data',
            name='title',
        ),
        migrations.AddField(
            model_name='data',
            name='committee',
            field=models.ManyToManyField(blank=True, to='legislative.committees'),
        ),
        migrations.AddField(
            model_name='data',
            name='hierarchy',
            field=models.ManyToManyField(blank=True, to='legislative.hierarchy'),
        ),
        migrations.AddField(
            model_name='data',
            name='subcommittee',
            field=models.ManyToManyField(blank=True, to='legislative.subcommittees'),
        ),
        migrations.AddField(
            model_name='data',
            name='title',
            field=models.ManyToManyField(blank=True, to='legislative.title'),
        ),
    ]
