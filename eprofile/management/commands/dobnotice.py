# !/hungntpl/.local/bin/python
# coding=utf-8
# Sending notice email about end of contract date
from django.core.management.base import BaseCommand, CommandError
from eprofile.models import efile
from django.core.mail import send_mail
import datetime


class Command(BaseCommand):
    help = 'Report birhday'

    def handle(self, *args, **options):
#        try:
#            epis = epidamic.objects.all()
#            for epi in epis:
#                 self.stdout.write(self.style.SUCCESS(epi.idemp))
#        except epidamic.DoesNotExist:
#            self.stdout.write(self.style.ERROR('Field "idemp" does not exist.'))
#            return
#
#        self.stdout.write(self.style.SUCCESS('Successfully printed all employee ID'))
        final_list = ''
#        try:
#            epis = epidamic.objects.filter(tempchektime__date = datetime.date.today())
#            for epi in epis:
#                idlist = idlist + str(epi.idemp) + ', '
#        except epidamic.DoesNotExist:
#                idlist = 'không tồn tại'

#        idlist = idlist + '\n'


        #dobemp_list = efile.objects.filter(dob__date = datetime.date.today())
        temp_list = efile.objects.filter(dob__month = datetime.date.today().month,dob__day = datetime.date.today().day)
        dobemp_list = temp_list.exclude(sec = "QUIT")

        for emp in dobemp_list:
            final_list = final_list + str(emp.dob) + ':' + str(emp.sec) + '-' + str(emp.idemp) + ':' + str(emp.firstname) + ' ' + str(emp.midname) + ' ' + str(emp.lastname) + '\n'
        if dobemp_list.exists():
            send_mail(
                    'Date of birth - Danh sách NLĐ VNSP sinh nhật hôm nay ' + str(datetime.date.today()),
                    'Danh sách sinh nhật hôm nay ' + '\n' + str(final_list), # + str(obj.idemp) + "(" + fname + " " + mname + " " + lname + "): " + str(obj.etemp) + " °C", #'Subject',
                    'support@vnsp.vn', # Reciver ['hungntpl@gmail.com', 'hungnt@vnsp.vn'],
                    ['hungnt@vnsp.vn','thuyttt@vnsp.vn','all.manager@vnsp.vn'],
                    #['hungnt@vnsp.vn'],
                )
        return