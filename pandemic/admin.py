from django.contrib import admin
from .models import * #, empProxy
#from django.contrib.auth.models import User
from eprofile.models import efile
import datetime
import csv
from django.http import HttpResponse

from django.core.mail import send_mail
from django.utils.html import format_html

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RreceiverAdmin(admin.ModelAdmin):
    list_display = ('fname','email')
    #list_editable = ('fname','email')
    list_display_links = ('fname','email')
admin.site.register(Rreceivers,RreceiverAdmin)

class epidemicResource(resources.ModelResource):

    class Meta:
        model = epidamic
        import_id_fields = ['idemp']

class epidemicAdmin(ImportExportModelAdmin):
    resource_class = epidemicResource

    list_display = ('sec','idemp','fname','tempchektime','fkind','etemp','ckind','hkind','bkind','remarks')
    readonly_fields = ['idemp','tempchektime','fkind']
    list_display_links = ['sec','idemp','fname','tempchektime']
    search_fields = ('idemp__idemp','tempchektime')
    # search_fields = ('sec','idemp__idemp','tempchektime')
    list_filter = ['fkind','ckind','hkind','bkind','tempchektime']

    def save_model(self, request, obj, form, change):
        obj.idemp  = efile.objects.get(idemp=request.user.username)
        sec = efile.objects.get(idemp=request.user.username).sec
        fname = efile.objects.get(idemp=request.user.username).firstname
        mname = efile.objects.get(idemp=request.user.username).midname
        lname = efile.objects.get(idemp=request.user.username).lastname
        
        if obj.etemp > 37:
            obj.fkind = "C"
        obj.save()
        if obj.etemp > 37 or obj.ckind == "C" or obj.hkind == "C" or obj.bkind == "C":
            for per in Rreceivers.objects.all():
                send_mail(
                    'Epidemic alert - Cảnh báo dịch tễ',
                    'Nhân viên có đấu hiệu nghi ngờ: ' +'\n' + '\n' + 
                    sec + ':' + str(obj.idemp) + "-" + fname + " " + mname + " " + lname + '\n' +
                    '       Thân nhiệt:                             ' + str(obj.etemp) + " °C" + '\n' +
                    '       Ho ?:                                        ' + obj.get_ckind_display() + '\n' +
                    '       Đau đầu ?:                              ' + obj.get_hkind_display() + '\n' +
                    '       Tức ngực ?:                            ' + obj.get_bkind_display() + '\n' +
                    '       Thời điểm khai báo:              ' + str(datetime.datetime.now()), #'Subject',
                    #'Thân nhiệt cao ' + str(obj.idemp) + "(" + str(obj.fname) + "): " + str(obj.etemp) + " °C", #'Subject',
                    'safety@vnsp.vn', # Reciver ['hungntpl@gmail.com', 'hungnt@vnsp.vn'],
                    [per.email],
                )
            
        

    def get_readonly_fields(self, request, obj=None):
        #if request.user.is_superuser:
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return [] # Superuser is unlimited, imange_tag needed readonly property
        return self.readonly_fields


    
admin.site.register(epidamic,epidemicAdmin)

# class epidAdmin(admin.ModelAdmin):


#     list_display = ('sec','idemp','fname','tempchektime','fkind','etemp','ckind','hkind','bkind','remarks')
#     readonly_fields = ['idemp','tempchektime','fkind']
#     list_display_links = ['sec','idemp','fname','tempchektime']
#     search_fields = ('idemp__idemp','tempchektime')
#     # search_fields = ('sec','idemp__idemp','tempchektime')
#     list_filter = ['fkind','ckind','hkind','bkind','tempchektime']
   
#     actions = ['export_as_csv']

#     def export_as_csv(self,request,queryset):
#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]

#         response = HttpResponse(content_type='text/csv')
#         #response.write(codecs.BOM_UTF8)
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

#         response.write(u'\ufeff'.encode('utf8'))
#         writer = csv.writer(response)

#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])

#         return response

#     export_as_csv.short_description = "Xuất dữ liệu ra Excel"


#     def save_model(self, request, obj, form, change):
#         obj.idemp  = efile.objects.get(idemp=request.user.username)
#         sec = efile.objects.get(idemp=request.user.username).sec
#         fname = efile.objects.get(idemp=request.user.username).firstname
#         mname = efile.objects.get(idemp=request.user.username).midname
#         lname = efile.objects.get(idemp=request.user.username).lastname
        
#         if obj.etemp > 37:
#             obj.fkind = "C"
#         obj.save()
#         if obj.etemp > 37 or obj.ckind == "C" or obj.hkind == "C" or obj.bkind == "C":
#             for per in Rreceivers.objects.all():
#                 send_mail(
#                     'Epidemic alert - Cảnh báo dịch tễ',
#                     'Nhân viên có đấu hiệu nghi ngờ: ' +'\n' + '\n' + 
#                     sec + ':' + str(obj.idemp) + "-" + fname + " " + mname + " " + lname + '\n' +
#                     '       Thân nhiệt:                             ' + str(obj.etemp) + " °C" + '\n' +
#                     '       Ho ?:                                        ' + obj.get_ckind_display() + '\n' +
#                     '       Đau đầu ?:                              ' + obj.get_hkind_display() + '\n' +
#                     '       Tức ngực ?:                            ' + obj.get_bkind_display() + '\n' +
#                     '       Thời điểm khai báo:              ' + str(datetime.datetime.now()), #'Subject',
#                     #'Thân nhiệt cao ' + str(obj.idemp) + "(" + str(obj.fname) + "): " + str(obj.etemp) + " °C", #'Subject',
#                     'safety@vnsp.vn', # Reciver ['hungntpl@gmail.com', 'hungnt@vnsp.vn'],
#                     [per.email],
#                 )
            
        

#     def get_readonly_fields(self, request, obj=None):
#         #if request.user.is_superuser:
#         if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
#             return [] # Superuser is unlimited, imange_tag needed readonly property
#         return self.readonly_fields


#     # def get_queryset(self, request):
#     #     return chain(super().get_queryset(request), efile)
#         #return super().get_queryset(request)
#     # def get_queryset(self, request):

#     #     if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
#     #         return super().get_queryset(request).filter(idemp=request.user.username)
#     #     else:
#     #         return super().get_queryset(request)

# admin.site.register(epidamic,epidAdmin)

# class empepidAdmin(admin.ModelAdmin):
#      list_display = ('idemp','fname')
#      readonly_fields = ('idemp','fname')

# admin.site.register(empProxy,empepidAdmin)
