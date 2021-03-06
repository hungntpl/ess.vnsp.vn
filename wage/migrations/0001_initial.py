# Generated by Django 3.1.7 on 2021-03-13 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sday', models.DateField(blank=True, null=True, verbose_name='Ngày bắt đầu kỳ lương')),
                ('fday', models.DateField(blank=True, null=True, verbose_name='Ngày kết thúc kỳ lương')),
                ('fullname', models.CharField(blank=True, max_length=35, null=True, verbose_name='Họ và tên')),
                ('contsal', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Lương theo hợp đồng')),
                ('dedoffwork', models.CharField(blank=True, max_length=50, null=True, verbose_name='Deduction offwork')),
                ('bwagepay', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Lương cơ bản phải trả (Lương HĐLĐ trừ số bị trừ do nghỉ việc)')),
                ('w4overtime', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Lương làm thêm giờ (Lương HĐLĐ/175* số giờ thực làm thêm * 150% hoặc 200% hoặc 400%)')),
                ('twoshiftallow', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Trợ cấp ca ngày (60,000 * số ngày thực làm ca ngày/số ngày lv của công ty)')),
                ('treeshiftallow', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Phụ cấp của ngày làm ca 3 (90,000 * số ngày thực làm ca 3/số ngày lv của công ty)')),
                ('siallow', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Nghỉ bảo hiểm xã hội')),
                ('fullattendbonus', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Thưởng chuyên cần')),
                ('adjustsf', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Phụ cấp ATLĐ, PCCC')),
                ('otherallow', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Thưởng đặc biệt hoặc điều chỉnh khác')),
                ('specialbnif', models.CharField(blank=True, max_length=200, null=True, verbose_name='Lý do thưởng/điều chỉnh')),
                ('ttlpretaxincome', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Tổng thu nhập trước thuế')),
                ('siui', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='BHXH (8%) + BH Thất nghiệp (1%)')),
                ('hi', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Bảo hiểm Ytế (1,5% lương HĐLĐ)')),
                ('adj43shift', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Các khoản điều chỉnh tăng giảm đối với sản xuất 3 ca')),
                ('incomnop', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Income N-O-P')),
                ('exw4nightwork', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Lương làm thêm do làm đêm')),
                ('transfee', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Trợ cấp đi lại')),
                ('ttladjustbg', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Total')),
                ('ttlincome', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Total income')),
                ('tradeuni', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Lệ phí công đoàn')),
                ('inctax', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Thuế thu nhập cá nhân tạm tính')),
                ('de4motofee', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Trả góp mua xe máy')),
                ('otherdec', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Các khoản khấu trừ khác')),
                ('subttldeduc', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='sub total deduction')),
                ('netpay', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Tổng số tiền nhận được')),
                ('ttldeduction', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True, verbose_name='Total deduction')),
                ('bankname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên ngân hàng')),
                ('bankacc', models.CharField(blank=True, max_length=25, null=True, verbose_name='Số tài khoản thụ hưởng')),
                ('aleave', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tổng phép năm')),
                ('alpreuse', models.CharField(blank=True, max_length=50, null=True, verbose_name='Số ngày đã dùng')),
                ('alcuruse', models.CharField(blank=True, max_length=50, null=True, verbose_name='Số dùng trong kỳ')),
                ('alremain', models.CharField(blank=True, max_length=50, null=True, verbose_name='Số ngày còn lại')),
                ('otherdecremark', models.CharField(blank=True, max_length=50, null=True, verbose_name='Lý do khấu trừ khác')),
                ('idemp', models.ForeignKey(default=None, max_length=15, on_delete=django.db.models.deletion.CASCADE, to='eprofile.efile', verbose_name='Số ID')),
            ],
            options={
                'verbose_name': 'wage notice',
                'verbose_name_plural': '1. Thông báo lương',
            },
        ),
        migrations.CreateModel(
            name='ts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tsday', models.DateField(blank=True, null=True, verbose_name='Ngày')),
                ('wshift', models.CharField(blank=True, max_length=5, null=True, verbose_name='Ca làm việc')),
                ('SH', models.CharField(blank=True, max_length=6, null=True, verbose_name='Giờ bắt đầu')),
                ('SM', models.CharField(blank=True, max_length=6, null=True, verbose_name='Phút bắt đầu')),
                ('FH', models.CharField(blank=True, max_length=6, null=True, verbose_name='Giờ kết thúc')),
                ('FM', models.CharField(blank=True, max_length=6, null=True, verbose_name='Phút kết thúc')),
                ('NT', models.CharField(blank=True, max_length=30, null=True, verbose_name='Normal time')),
                ('NTShift', models.CharField(blank=True, max_length=30, null=True, verbose_name='Normal time shift')),
                ('OTNight', models.CharField(blank=True, max_length=30, null=True, verbose_name='Overtime night')),
                ('Hol2Day', models.CharField(blank=True, max_length=30, null=True, verbose_name='200% ngày')),
                ('Hol2Night', models.CharField(blank=True, max_length=30, null=True, verbose_name='200% đêm')),
                ('Hol3Day', models.CharField(blank=True, max_length=30, null=True, verbose_name='300% ngày')),
                ('Hol3Night', models.CharField(blank=True, max_length=30, null=True, verbose_name='300% đêm')),
                ('idemp', models.ForeignKey(default=None, max_length=15, on_delete=django.db.models.deletion.CASCADE, to='eprofile.efile', verbose_name='Số ID')),
            ],
            options={
                'verbose_name': 'time sheet',
                'verbose_name_plural': '2. Chi tiết ngày công',
            },
        ),
    ]
