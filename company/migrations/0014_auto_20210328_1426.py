# Generated by Django 3.1.7 on 2021-03-28 07:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20210328_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='idate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Ngày'),
        ),
    ]