# Generated by Django 3.1.7 on 2021-03-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_auto_20210328_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='idemp',
            field=models.CharField(blank=True, default=None, max_length=15, null=True, verbose_name='Emp ID'),
        ),
    ]
