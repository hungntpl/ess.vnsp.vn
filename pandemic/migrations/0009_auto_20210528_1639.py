# Generated by Django 3.1.7 on 2021-05-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0008_auto_20210527_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epidamic',
            name='bkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Trong 14 ngày qua anh/chị có tiếp xúc với người bệnh hoặc người nghi nhiễm mắc Covid-19 hay không?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='ckind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Ho khan/Cough ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='etemp',
            field=models.FloatField(default=36.6, max_length=5, verbose_name='Thân nhiệt/body temperature ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='fkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Sốt/Fever ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='hkind',
            field=models.CharField(choices=[('C', 'Yes'), ('K', 'No')], default='K', max_length=1, verbose_name='Đau họng/Sore throat ?'),
        ),
        migrations.AlterField(
            model_name='epidamic',
            name='remarks',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Trong vòng 14 ngày qua, Anh/Chị có đến tỉnh/thành phố, quốc gia/vùng lãnh thổ nào (Có thể đi qua nhiều nơi)In the past 14 days, have you been to any province/city/territory/country? If yes, where?:'),
        ),
    ]
