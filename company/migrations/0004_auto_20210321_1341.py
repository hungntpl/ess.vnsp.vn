# Generated by Django 3.1.7 on 2021-03-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20210321_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answ',
            field=models.TextField(default=None, max_length=500, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='quest',
            field=models.TextField(default=None, max_length=500, verbose_name='Question'),
        ),
    ]