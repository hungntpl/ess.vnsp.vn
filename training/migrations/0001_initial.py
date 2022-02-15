# Generated by Django 3.1.7 on 2021-03-13 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='iso9index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(default=None, max_length=255, verbose_name='Section')),
            ],
            options={
                'verbose_name': 'ISO 9001 standard',
                'verbose_name_plural': '4. ISO 9001',
            },
        ),
        migrations.CreateModel(
            name='isoindex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdname', models.CharField(default=None, max_length=255, verbose_name='Section')),
            ],
            options={
                'verbose_name': 'ISO 14001 standard',
                'verbose_name_plural': '3. ISO 14001',
            },
        ),
        migrations.CreateModel(
            name='tnindex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default=None, max_length=255, verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': '1. Knowledge Center',
            },
        ),
        migrations.CreateModel(
            name='wclendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên tài liệu')),
                ('wcpic', models.ImageField(null=True, upload_to='workingcalendar', verbose_name='Ảnh gốc')),
            ],
            options={
                'verbose_name': 'Working Calendar',
                'verbose_name_plural': '2. Lịch làm việc',
            },
        ),
        migrations.CreateModel(
            name='tnsection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên tài liệu')),
                ('docfile', models.FileField(default=None, upload_to='documents/%Y/%m/%d', verbose_name='Link download')),
                ('sid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.tnindex', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'Section database',
            },
        ),
        migrations.CreateModel(
            name='isodetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên tài liệu')),
                ('docfile', models.FileField(default=None, upload_to='documents/%Y/%m/%d', verbose_name='Link download')),
                ('sid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.isoindex', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'standard name',
            },
        ),
        migrations.CreateModel(
            name='iso9detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên tài liệu')),
                ('docfile', models.FileField(default=None, upload_to='documents/%Y/%m/%d', verbose_name='Link download')),
                ('sid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.iso9index', verbose_name='ID')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'standard name',
            },
        ),
    ]