from django.contrib import admin
from .models import ntboard, safetybd, qualitybd, prdbd, vnspgallery
from django.core.mail import send_mail
from smtplib import SMTPException
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import format_html
# from django.core.mail.exceptions import EmailError

from eprofile.models import efile

# Redirect to gallery
class vnspgalleryAdmin(admin.ModelAdmin):
    # def custom_redirect(self, sender, instance, **kwargs):
    #     return HttpResponseRedirect('/vnspgallery')
    list_display = ('doctitle','show_firm_url')

    def show_firm_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.hlink)

    show_firm_url.short_description = "Firm URL"

admin.site.register(vnspgallery,vnspgalleryAdmin)
# Other board
class ntbAdmin(admin.ModelAdmin):

    list_display = ('doctitle','dateissue','docfile')
    
    actions = ['broadcast']

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            if 'broadcast' in actions:
                del actions['broadcast']
                #del actions['import_system_user234']
        return actions

    def broadcast(self,request,queryset):
        content = ""
        for qe in queryset:
            content = content + str(qe.doctitle) + ': http://' + request.META['HTTP_HOST'] + qe.docfile.url + '\n' + '\n' 
        
        

        for per in efile.objects.exclude(sec__iexact="QUIT"):
            if per.email != None :
                try:
                    send_mail(
                        'Cổng thông tin VNSP - Bảng tin thông báo điện tử ' ,
                        'Thân chào ID: ' + str(per.idemp) + ' - ' + str(per.firstname) +' '+ str(per.midname) +' '+ str(per.lastname) + '\n' + '\n' +
                        'Bạn nhận được email này từ phòng HCNS của công ty VNSP.' + '\n' + '\n' +
                        'Bản tin chi tiết ở link sau:' + '\n' + '\n' + 
                        content + '\n' + '\n' + 
                        'Chú ý: Không trả lời email tự động này' + '\n' + '\n' + 
                        'Xin cảm ơn !!!' + '\n' + 
                        'Phòng HCNS VNSP', 
                        'adm@vnsp.vn', # Sender
                        [per.email], # Receiver 
                        #['hungnt@vnsp.vn'], # Receiver  
                        fail_silently=False,
                    )
                    self.message_user(request, 'Đã gửi tới ID:' + str(per.idemp) + '-' + str(per.email))

                except SMTPException as e:
                    messages.add_message(request, messages.INFO, 'Error happended with ID: ' + str(per.idemp) + ' ' + str(e))
                          
                    
    broadcast.short_description = "Gửi bản tin đã chọn cho toàn bộ CNV"
        
        # print(obj, type(obj))
        # self.message_user(request, "Đã gửi email nhắc nhở tới ...")
        #for per in efile.objects.exclude(sec__iexact="QUIT"):
        # for per in efile.objects.filter(sec__iexact="QUIT").exclude(email__isnull=True):
            # self.message_user(request, "Đã xảy ra lỗi với email của " + str(per.sec) + ': ' + str(per.idemp) + ' '+ str(per.firstname) +
            # ' ' + str(per.midname) + ' ' + str(per.lastname))
            
            # try:
            #     send_mail(
            #         'Cổng thông tin VNSP - Bảng tin thông báo điện tử ' ,
            #         'Thân chào ' + str(per.firstname() + ' ' + str(per.midname) + ' ' + str(per.lastname) + '\n' + '\n' +
            #         'Bạn nhận được email này từ phòng HCNS của công ty VNSP.' + '\n' + '\n' +
            #         'Bản tin:  "' + str(obj.doctitle) +' " chi tiết ở link sau:' + '\n' + '\n' + 
            #         'http://' + request.META['HTTP_HOST'] + obj.docfile.url + '\n' + '\n' + '\n' +
            #         'Chú ý: Không trả lời email tự động này' + '\n' + '\n' + 
            #         'Xin cảm ơn !!!' + '\n' + 
            #         'Phòng HCNS VNSP', 
            #         'adm@vnsp.vn', # Sender
            #         [per.email], # Receiver
            #         #['hungnt@vnsp.vn'], # Receiver  
            #         fail_silently=True,
            #     )   
            # except FooException as exc:
            #     if exc.err_code == 42:
            #         logger.exception("...")
            #     raise
            # except EmailError:
            #     pass



            #except SMTPException as e:
            # except:
            #     self.message_user(request, "Đã xảy ra lỗi với email của " + str(per.sec) + ': ' + str(per.idemp) + ' '+ str(per.firstname) + ' ' + str(per.midname) + ' ' + str(per.lastname))
                #self.message_user(request, "Đã xảy ra lỗi với email của ", e)
                #print('There was an error sending an email: ', e) 

                
                       
        # return super().response_add(request, obj, post_url_continue)

    # def response_add(self, request, obj, post_url_continue=None):
    #     # Make sure ?language=... is included in the redirects.
    #     self.message_user(request, "Đã gửi email nhắc nhở tới ...")
    #     #redirect = super().response_add(request, obj, post_url_continue)
    #     return self._patch_redirect(request, obj, redirect)
    
admin.site.register(ntboard,ntbAdmin)

# Savety board
class safbAdmin(admin.ModelAdmin):

    list_display = ('doctitle','dateissue','docfile')
    ordering = ['doctitle']
    actions = ['broadcast']

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists() or request.user.groups.filter(name='hse').exists()):
            if 'broadcast' in actions:
                del actions['broadcast']
                #del actions['import_system_user234']
        return actions

    def broadcast(self,request,queryset):
        content = ""
        for qe in queryset:
            content = content + str(qe.doctitle) + ': http://' + request.META['HTTP_HOST'] + qe.docfile.url + '\n' + '\n' 
        
        

        for per in efile.objects.exclude(sec__iexact="QUIT"):
            if per.email != None :
                try:
                    send_mail(
                        'Cổng thông tin VNSP - Bảng tin an toàn & 5S' ,
                        'Thân chào ID: ' + str(per.idemp) + ' - ' + str(per.firstname) +' '+ str(per.midname) +' '+ str(per.lastname) + '\n' + '\n' +
                        'Bạn nhận được email này từ phòng HCNS của công ty VNSP.' + '\n' + '\n' +
                        'Bản tin chi tiết ở link sau:' + '\n' + '\n' + 
                        content + '\n' + '\n' + 
                        'Chú ý: Không trả lời email tự động này' + '\n' + '\n' + 
                        'Xin cảm ơn !!!' + '\n' + 
                        'Phòng HCNS VNSP', 
                        'adm@vnsp.vn', # Sender
                        [per.email], # Receiver 
                        #['hungnt@vnsp.vn'], # Receiver  
                        fail_silently=False,
                    )
                    self.message_user(request, 'Đã gửi tới ID:' + str(per.idemp) + '-' + str(per.email))

                except SMTPException as e:
                    messages.add_message(request, messages.INFO, 'Error happended with ID: ' + str(per.idemp) + ' ' + str(e))
                          
                    
    broadcast.short_description = "Gửi bản tin đã chọn cho toàn bộ CNV"
        
    # readonly_fields = ['doctitle','docfile']
    # def get_readonly_fields(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='notice_board_public').exists() or request.user.groups.filter(name='manager').exists()):
    #         #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
    #         return []
    #     return self.readonly_fields


admin.site.register(safetybd,safbAdmin)

# Quality board
class quabAdmin(admin.ModelAdmin):

    list_display = ('doctitle','dateissue','docfile')
    ordering = ['doctitle']
    actions = ['broadcast']

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            if 'broadcast' in actions:
                del actions['broadcast']
                #del actions['import_system_user234']
        return actions

    def broadcast(self,request,queryset):
        content = ""
        for qe in queryset:
            content = content + str(qe.doctitle) + ': http://' + request.META['HTTP_HOST'] + qe.docfile.url + '\n' + '\n' 
        
        

        for per in efile.objects.exclude(sec__iexact="QUIT"):
            if per.email != None :
                try:
                    send_mail(
                        'Cổng thông tin VNSP - Bảng tin chất lượng ' ,
                        'Thân chào ID: ' + str(per.idemp) + ' - ' + str(per.firstname) +' '+ str(per.midname) +' '+ str(per.lastname) + '\n' + '\n' +
                        'Bạn nhận được email này từ phòng HCNS của công ty VNSP.' + '\n' + '\n' +
                        'Bản tin chi tiết ở link sau:' + '\n' + '\n' + 
                        content + '\n' + '\n' + 
                        'Chú ý: Không trả lời email tự động này' + '\n' + '\n' + 
                        'Xin cảm ơn !!!' + '\n' + 
                        'Phòng HCNS VNSP', 
                        'adm@vnsp.vn', # Sender
                        [per.email], # Receiver 
                        #['hungnt@vnsp.vn'], # Receiver  
                        fail_silently=False,
                    )
                    self.message_user(request, 'Đã gửi tới ID:' + str(per.idemp) + '-' + str(per.email))

                except SMTPException as e:
                    messages.add_message(request, messages.INFO, 'Error happended with ID: ' + str(per.idemp) + ' ' + str(e))
                          
                    
    broadcast.short_description = "Gửi bản tin đã chọn cho toàn bộ CNV"
        
    # readonly_fields = ['doctitle','docfile']
    # def get_readonly_fields(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='notice_board_public').exists() or request.user.groups.filter(name='manager').exists()):
    #         #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
    #         return []
    #     return self.readonly_fields


admin.site.register(qualitybd,quabAdmin)

# Production board
class prdbAdmin(admin.ModelAdmin):

    list_display = ('doctitle','dateissue','docfile')
    ordering = ['doctitle']
    actions = ['broadcast']

    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            if 'broadcast' in actions:
                del actions['broadcast']
                #del actions['import_system_user234']
        return actions

    def broadcast(self,request,queryset):
        content = ""
        for qe in queryset:
            content = content + str(qe.doctitle) + ': http://' + request.META['HTTP_HOST'] + qe.docfile.url + '\n' + '\n' 
        
        

        for per in efile.objects.exclude(sec__iexact="QUIT"):
            if per.email != None :
                try:
                    send_mail(
                        'Cổng thông tin VNSP - Bảng tin sản xuất ' ,
                        'Thân chào ID:' + str(per.idemp) + '-' + str(per.firstname) +' '+ str(per.midname) +' '+ str(per.lastname) + '\n' + '\n' +
                        'Bạn nhận được email này từ phòng HCNS của công ty VNSP.' + '\n' + '\n' +
                        'Bản tin chi tiết ở link sau:' + '\n' + '\n' + 
                        content + '\n' + '\n' + 
                        'Chú ý: Không trả lời email tự động này' + '\n' + '\n' + 
                        'Xin cảm ơn !!!' + '\n' + 
                        'Phòng HCNS VNSP', 
                        'adm@vnsp.vn', # Sender
                        [per.email], # Receiver 
                        #['hungnt@vnsp.vn'], # Receiver  
                        fail_silently=False,
                    )
                    self.message_user(request, 'Đã gửi tới ID:' + str(per.idemp) + '-' + str(per.email))

                except SMTPException as e:
                    messages.add_message(request, messages.INFO, 'Error happended with ID: ' + str(per.idemp) + ' ' + str(e))
                          
                    
    broadcast.short_description = "Gửi bản tin đã chọn cho toàn bộ CNV"
        
    # readonly_fields = ['doctitle','docfile']
    # def get_readonly_fields(self, request, obj=None):
    #     if (request.user.is_superuser or request.user.groups.filter(name='notice_board_public').exists() or request.user.groups.filter(name='manager').exists()):
    #         #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
    #         return []
    #     return self.readonly_fields


admin.site.register(prdbd,prdbAdmin)