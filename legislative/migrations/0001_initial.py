# Generated by Django 4.1.12 on 2024-01-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('hierarchy', models.CharField(blank=True, max_length=512, null=True)),
                ('link', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('district', models.CharField(blank=True, max_length=128, null=True)),
                ('party', models.CharField(blank=True, max_length=128, null=True)),
                ('employer', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=512, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image_name', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCommittees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('hierarchy', models.CharField(blank=True, max_length=512, null=True)),
                ('link', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]
