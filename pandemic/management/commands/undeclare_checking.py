# !/hungntpl/.local/bin/python
# coding=utf-8
from django.core.management.base import BaseCommand, CommandError
from pandemic.models import *
from eprofile.models import efile
from django.core.mail import send_mail
import datetime
# from django.utils import timezone

class Command(BaseCommand):
    help = 'Prints all ID in the database'

    def handle(self, *args, **options):

        final_list = ''
        # epis = epidamic.objects.filter(tempchektime__contains = timezone.localtime(timezone.now()).date())
        epis = epidamic.objects.filter(tempchektime__gt = datetime.date.today())
        epi_list = [idemp for idemp in epis]
#        emps = efile.objects.exclude(sec = "QUIT",idemp__in = epi_list)
        temp_list = efile.objects.exclude(idemp__in = epi_list)

        non_report_list = temp_list.exclude(sec = "QUIT")

#        non_report_list = temp_list1.exclude(sec = "PQ")

        for emp in non_report_list:
            final_list = final_list + str(emp.sec) + '-' + str(emp.idemp) + ':      ' + str(emp.firstname) + ' ' + str(emp.midname) + ' ' + str(emp.lastname) + '\n'
        for per in Rreceivers.objects.all():
                send_mail(
                'Epidemic alert - Danh sách chưa khai báo dịch tễ ngày ' + str(datetime.date.today()),
                'Danh sách chưa khai báo ' + '\n' + str(final_list), # + str(obj.idemp) + "(" + fname + " " + mname + " " + lname + "): " + str(obj.etemp) + " °C", #'Subject',
                #'Thân nhiệt cao ' + str(obj.idemp) + "(" + str(obj.fname) + "): " + str(obj.etemp) + " °C", #'Subject',
                'safety@vnsp.vn', # Sender
                [per.email], # Reciever
            )

        
        return