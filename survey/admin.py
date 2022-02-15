from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime
from .models import cotrip, s360d, cotmem, quiz
from eprofile.models import efile
from datetime import datetime 
from django.utils.timezone import now
from django.utils import timezone
from django.utils.html import format_html
import csv
from django.http import HttpResponse
# from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# class ctmemResource(resources.ModelResource):
#     class Meta:
#         model = cotmem
class ctmemResource(resources.ModelResource):

    class Meta:
        model = cotmem
        import_id_fields = ['idemp']
class ctmemAdmin(ImportExportModelAdmin):
    list_display = ('ctdid','fullname','mkid','dob')
    #readonly_fields = ['ctdid','mkid','dob','fullname']
    list_editable = ('fullname','mkid','dob')
    readonly_fields = ['ctdid']
    actions = ['export_as_csv']

    # Remove normal user see the other persion
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(ctdid__idemp=request.user.username)
        else:
            return super().get_queryset(request)
    # Export data
    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        #response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Xuất dữ liệu thành viên đi cùng"

    # def has_delete_permission(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
    #         return True
    # def has_change_permission(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
    #         return True
    # def has_add_permission(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
    #         return True

    #resource_class = ctmemResource
admin.site.register(cotmem,ctmemAdmin)

class ctmemInline(admin.TabularInline):
    model = cotmem
    extra = 0

class cotripResource(resources.ModelResource):

    class Meta:
        model = cotrip
        import_id_fields = ['idemp']
class cotripAdmin(ImportExportModelAdmin):
    #resource_class = ctResource
    list_display = ('idemp','gfname','ctyear','jkind','thumbnail')
    search_fields = ('idemp__idemp', 'ctyear') # Don't filter on a ForeignKey field itself! add __foreignKeyfieldname ; name represents the field-name from the table that we have a ForeinKey relationship with.
    list_display_links = ['idemp','gfname','ctyear']
    readonly_fields = ['idemp','ctyear','ctremarks','image_tag','docfile']
    ordering = ['idemp']
    #list_filter = ('jkind', 'ctyear')

    def gfname(self, request): # Get fullname
        return efile.objects.get(idemp=request.idemp).fname()
    gfname.short_description = 'Họ và tên'

    def get_list_filter(self, request):
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['jkind', 'ctyear']
        else:
            return []
    fieldsets = [
        ('Thông tin chung',               {'fields': (('ctyear','ctremarks','docfile'))}),
        #('Ảnh thực tế',             {'fields': ['mempic']}),
        ('Phản hồi, ảnh thực tế hoạt động',             {'fields': ('idemp','jkind','feedbacks','image_tag','mempic')}),
        ]

    def image_tag(self, obj):
        if obj.mempic and hasattr(obj.mempic, 'url'):
            return format_html('<img src="{0}" style="width: auto; height:260px;" />'.format(obj.mempic.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def thumbnail(self, obj):
        if obj.mempic and hasattr(obj.mempic, 'url'):
            return format_html('<img src="{0}" style="width: auto; height:100px;" />'.format(obj.mempic.url))

    thumbnail.short_description = 'thumbnail'
    thumbnail.allow_tags = True

    def get_readonly_fields(self, request, obj=None):
        #if request.user.is_superuser:
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
        return self.readonly_fields

    inlines = [
        ctmemInline,
    ]


    actions = ['import_all_user','export_as_csv']

    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        #response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected to csv format"

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            if 'import_all_user' in actions:
                del actions['import_all_user']
                #del actions['import_system_user234']
        return actions

    # Remove normal user see the other persion
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)


    def import_all_user(self,request,queryset):

    # Get sample data
        for qe in queryset:
            ctyear = qe.ctyear
            ctremarks = qe.ctremarks
            docfile = qe.docfile
    # Copy username from User table
        # for qe in efile.objects.all():
        for qe in efile.objects.exclude(sec__contains="QUIT"):    
            ctid = qe.idemp
            # messages.add_message(request, messages.INFO, ctid)
            #if not cotrip.objects.filter(idemp=ctid).exists():
            cotuser = cotrip(idemp=qe,ctyear=ctyear,docfile=docfile,ctremarks=ctremarks)
            cotuser.save()

    import_all_user.short_description = "Thêm nhân viên từ danh sách profile theo mẫu đã chọn"
admin.site.register(cotrip,cotripAdmin)

class s360dResource(resources.ModelResource):

    class Meta:
        model = s360d
        import_id_fields = ['idemp']
class s360dAdmin(ImportExportModelAdmin):
    list_display = ('idemp','comment','remarks')

    actions = ['export_as_csv', 'export_as_exl']
    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        #response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected to csv"

    #actions = ['export_as_exl']
    def export_as_exl(self,request,queryset):
        pass

    export_as_exl.short_description = "Export Selected to exl"

admin.site.register(s360d,s360dAdmin)


class quizResource(resources.ModelResource):

    class Meta:
        model = quiz
        import_id_fields = ['idemp']
class quizAdmin(ImportExportModelAdmin):
    #resource_class = ctResource
    list_display = ('idemp','gfname','ctyear','jkind','sameanswer','answertime')
    search_fields = ('idemp__idemp', 'ctyear') # Don't filter on a ForeignKey field itself! add __foreignKeyfieldname ; name represents the field-name from the table that we have a ForeinKey relationship with.
    list_display_links = ['idemp','gfname','ctyear']
    readonly_fields = ['idemp','ctyear','ctremarks','docfile','gfname','answertime','deadline']
    ordering = ['idemp']
    #list_filter = ('jkind', 'ctyear')

    def gfname(self, request): # Get fullname
        return efile.objects.get(idemp=request.idemp).fname()
    gfname.short_description = 'Họ và tên'


    def save_model(self, request, obj, form, change):
        obj.answertime = timezone.now()
        
        super().save_model(request, obj, form, change)


    def get_list_filter(self, request):
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists() ):
            return ['jkind', 'ctyear','sameanswer']
        else:
            return []
    fieldsets = [
        ('Thông tin chung',               {'fields': (('ctyear','ctremarks','docfile'))}),
        #('Ảnh thực tế',             {'fields': ['mempic']}),
        ('Phần trả lời',             {'fields': ('jkind','subanswer','sameanswer','idemp','gfname','answertime','deadline')}),
        ]


    def get_readonly_fields(self, request, obj=None):
        #if request.user.is_superuser:
        now = timezone.now()
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists() ):
            return ['gfname','answertime'] # Superuser is unlimited, imange_tag needed readonly property
        
        #elif request.GET['deadline'].fi < datetime.now():
        elif (obj.deadline != None) and (obj.deadline < now):
           return ['jkind','subanswer','idemp','ctyear','ctremarks','docfile','gfname','answertime','sameanswer','deadline']
           #return self.readonly_fields + ('jkind','sameanswer')

        return self.readonly_fields
        

        



    actions = ['import_all_user','export_as_csv']

    def export_as_csv(self,request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        #response.write(codecs.BOM_UTF8)
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected to csv format"

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists() ):
            if 'import_all_user' in actions:
                del actions['import_all_user']
            if 'export_as_csv' in actions:
                del actions['export_as_csv']
        return actions

    # Remove normal user see the other persion
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists() ):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)


    def import_all_user(self,request,queryset):

    # Get sample data
        for qe in queryset:
            ctyear = qe.ctyear
            ctremarks = qe.ctremarks
            docfile = qe.docfile
            deadline = qe.deadline
    # Copy username from User table
        # for qe in efile.objects.all():
        for qe in efile.objects.exclude(sec__contains="QUIT"):
            ctid = qe.idemp
            quizuser = quiz(idemp=qe,ctyear=ctyear,docfile=docfile,ctremarks=ctremarks,deadline=deadline)
            quizuser.save()

    import_all_user.short_description = "Thêm nhân viên từ danh sách profile theo mẫu đã chọn"

admin.site.register(quiz,quizAdmin)