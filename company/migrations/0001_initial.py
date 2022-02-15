# Generated by Django 3.1.7 on 2021-03-21 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(default=None, max_length=255, verbose_name='Question')),
                ('answ', models.CharField(default=None, max_length=255, verbose_name='Answer')),
                ('idate', models.DateField(default=django.utils.timezone.now, verbose_name='Issued date')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': '4. FAQ & Question',
            },
        ),
        migrations.CreateModel(
            name='OChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255, verbose_name='Title')),
                ('idate', models.DateField(default=django.utils.timezone.now, verbose_name='Issued date')),
                ('ocpic', models.ImageField(blank=True, null=True, upload_to='och', verbose_name='Statement')),
            ],
            options={
                'verbose_name': 'OCH',
                'verbose_name_plural': '2. Organization Chart',
            },
        ),
        migrations.CreateModel(
            name='PVM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255, verbose_name='Title')),
                ('idate', models.DateField(default=django.utils.timezone.now, verbose_name='Issued date')),
                ('pvmpic', models.ImageField(blank=True, null=True, upload_to='pvm', verbose_name='Statement')),
            ],
            options={
                'verbose_name': 'PVM',
                'verbose_name_plural': '1. Phylosophy - Vision - Mission',
            },
        ),
        migrations.CreateModel(
            name='SET',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa', models.CharField(default=None, max_length=255, verbose_name='FieldA')),
                ('fb', models.CharField(default=None, max_length=255, verbose_name='FieldB')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': '5. Setting',
            },
        ),
        migrations.CreateModel(
            name='WPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255, verbose_name='Title')),
                ('idate', models.DateField(default=django.utils.timezone.now, verbose_name='Issued date')),
                ('ocpic', models.ImageField(blank=True, null=True, upload_to='och', verbose_name='Statement')),
            ],
            options={
                'verbose_name': 'WPOST',
                'verbose_name_plural': '3. Working Positions',
            },
        ),
    ]