from django.contrib import admin

# Register your models here.
from .models import wn, ts
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class tsResource(resources.ModelResource):

    class Meta:
        model = ts
class wnResource(resources.ModelResource):

    class Meta:
        model = wn


class wnAdmin(ImportExportModelAdmin):
    #list_display = ('idemp','sday','fday','netpay')
    #list_display = ('idemp','cal_period','netpay','sday','fday')
    list_display = ('idemp','fullname','cal_period','netpay')
    list_display_links = ['idemp','cal_period']
    #list_filter = ['somefield']
    search_fields = ('idemp__idemp','fullname','sday','fday')
    resource_class = wnResource

    # if request.user.groups.filter(name='hrad').exists():
    #     @override_settings(IMPORT_EXPORT_EXPORT_PERMISSION_CODE='change')


    fieldsets = [
        ('Thông tin chung',               {'fields': ('idemp','fullname','contsal','sday','fday')}),
        ('Tổng số tiền nhận được (VNĐ):',             {'fields': ('netpay','bankname','bankacc')}),
        ('Các khoản nhận chịu thuế:',               {'fields': ('bwagepay',
                                                                'w4overtime',
                                                                'twoshiftallow',
                                                                'treeshiftallow',
                                                                'siallow',
                                                                'fullattendbonus',
                                                                'adjustsf',
                                                                'otherallow','specialbnif')}),
        ('Các khoản nhận giảm trừ trước thuế:',               {'fields': ('siui','hi','adj43shift')}),
        ('Thu nhập chịu thuế :',               {'fields': ('exw4nightwork','transfee')}),
        ('Các khoản trừ sau thuế:',               {'fields': ('tradeuni','inctax','de4motofee','otherdec','otherdecremark')}),
        ('Lịch sử nghỉ phép:',               {'fields': ('aleave','alpreuse','alcuruse','alremain')}),
       #('Detail: ',               {'fields': ['idemp']})
        ]



    # Prevent user from viewing other member info
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)

#    verbose_name = "Thông báo lương"
#    verbose_name_plural = "Salary notice"
    # def before_save_instance(self, instance, using_transactions, dry_run):
    #     format_str = '%d/%m/%y' # the format in which dates are stored in CSV file
    #     instance.edit_date = datetime.strptime(instance.edit_date, format_str)
    #     instance.premiere_date = datetime.strptime(instance.premiere_date, format_str)
    #     return instance


admin.site.register(wn,wnAdmin)


#class tsAdmin(admin.ModelAdmin):
class tsAdmin(ImportExportModelAdmin):
    list_display = ('idemp','tsday','wshift','SH','SM','FH','FM','NT','OTDay','NTShift','OTNight','Hol2Day','Hol2Night','Hol3Day','Hol3Night','AL','PP','UP','SI')
    resource_class = tsResource
    #search_fields = ('idemp__idemp')
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)


admin.site.register(ts,tsAdmin)