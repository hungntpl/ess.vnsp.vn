# Generated by Django 3.1.7 on 2021-05-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0010_auto_20210528_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epidamic',
            name='bkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Trong 14 ngày qua anh/chị có tiếp xúc với người bệnh hoặc người nghi nhiễm mắc Covid-19 hay không ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='ckind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Ho khan ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='etemp',
            field=models.FloatField(default=36.6, max_length=5, verbose_name='Thân nhiệt ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='fkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Sốt ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='hkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Đau họng ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='remarks',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Trong vòng 14 ngày qua, Anh/Chị có đến tỉnh/thành phố, quốc gia/vùng lãnh thổ nào (Có thể đi qua nhiều nơi)?'),
        ),
    ]
