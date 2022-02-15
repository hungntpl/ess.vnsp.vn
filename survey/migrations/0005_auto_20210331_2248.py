# Generated by Django 3.1.7 on 2021-03-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20210331_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='sameanswer',
            field=models.IntegerField(blank=True, null=True, verbose_name='Số người có cùng câu trả lời với bạn'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='ctyear',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên gọi - Topic'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='jkind',
            field=models.CharField(choices=[('A', 'Đáp án A'), ('B', 'Đáp án B'), ('C', 'Đáp án C'), ('D', 'Đáp án D'), ('E', 'Đáp án E'), ('F', 'Đáp án F')], default='A', max_length=1, verbose_name='Câu trả lời của bạn'),
        ),
    ]
