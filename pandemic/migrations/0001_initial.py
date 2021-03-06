# Generated by Django 3.1.7 on 2021-03-13 16:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empProxy',
            fields=[
            ],
            options={
                'verbose_name': 'epidemic report',
                'verbose_name_plural': '2. Lịch sử khai báo',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('eprofile.efile',),
        ),
        migrations.CreateModel(
            name='epidamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempchektime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Ngày giờ khai báo')),
                ('fkind', models.CharField(choices=[('C', 'Có sốt'), ('K', 'Không sốt')], default='K', max_length=1, verbose_name='Sốt ?')),
                ('etemp', models.FloatField(max_length=5, verbose_name='Thân nhiệt ?')),
                ('ckind', models.CharField(choices=[('C', 'Có ho khan'), ('K', 'Không ho khan')], default='K', max_length=1, verbose_name='Ho khan ?')),
                ('hkind', models.CharField(choices=[('C', 'Có đau đầu'), ('K', 'Không đau đầu')], default='K', max_length=1, verbose_name='Đau đầu ?')),
                ('bkind', models.CharField(choices=[('C', 'Có tức ngực, khó thở'), ('K', 'Không tức ngực, khó thở')], default='K', max_length=1, verbose_name='Tức ngực, khó thở ?')),
                ('remarks', models.TextField(blank=True, max_length=255, null=True, verbose_name='Ghi chú')),
                ('idemp', models.ForeignKey(default=None, max_length=15, on_delete=django.db.models.deletion.CASCADE, to='eprofile.efile', verbose_name='Số ID')),
            ],
            options={
                'verbose_name': 'epidemic logging',
                'verbose_name_plural': '1. Khai báo dịch tễ',
            },
        ),
    ]
