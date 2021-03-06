# Generated by Django 3.1.7 on 2021-05-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0007_auto_20210527_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epidamic',
            name='authkind',
            field=models.CharField(choices=[('C', 'Đã khai báo với chính quyền'), ('K', 'Chưa khai báo với chính quền')], default='C', max_length=1, verbose_name='Anh/chị đã khai báo ytế ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='bkind',
            field=models.CharField(choices=[('C', 'Có'), ('K', 'Không')], default='K', max_length=1, verbose_name='Trong 14 ngày qua anh/chị có tiếp xúc với người bệnh hoặc người nghi nhiễm mắc Covid-19 hay không?'),
        ),
    ]
