from django.contrib import admin
#from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
#from django.utils.html import mark_safe
from django.utils.html import format_html
#from django.urls import reverse
from .models import efile, famem, cert, helthcheck, wkhis, punaw #, wsec, wpost
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django.conf import settings





# Define Family memeber
class famemInline(admin.TabularInline):
    model = famem
    extra = 0

# Define Punish Award his
class pnInline(admin.TabularInline):
    model = punaw
    extra = 0


# Define Certificate
class certInline(admin.TabularInline):
    model = cert
    extra = 0


# wkhis Working history
class whInline(admin.TabularInline):
    model = wkhis
    extra = 0

class eprofileResource(resources.ModelResource):

    class Meta:
        model = efile
        import_id_fields = ['idemp']
class epAdmin(ImportExportModelAdmin):
    resource_class = eprofileResource
    list_display = ('thumbnail','sec','idemp','email','fname','dob','idno','gender')
    actions = ['import_system_user']
    list_display_links = ['thumbnail','sec','idemp','email']
    ordering = ['idemp']
    sortable_by = ['idemp','firstname','midname','lastname']
    search_fields = ['idemp', 'firstname', 'midname', 'lastname']
    #list_editable = ['sec','gender']
    #list_filter = ['sec','gender']

    readonly_fields = ['blood','idno','isno','sec','idemp','image_tag', 'firstname', 'midname', 'lastname','dob','healthlog','gender']
    list_per_page = 36

    fieldsets = [
        ('Ảnh đại diện',               {'fields': (('image_tag','headshot'))}),
        ('Ngoại hình, đồng phục, locker:',             {'fields': ('lockerno','height','weight','uniform',
                                                            'uneck','usoulder','uchest',
                                                            'uarm','ubelt','uback',
                                                            'ubelly','ubuttock','utrousers',
                                                            'shoes')}),
        #('Sức khỏe',               {'fields': (['blood'])}),
        ('Sức khỏe',               {'fields': (('blood','healthlog'))}),
        ('Thông tin khác:',             {'fields': ('isno','sec','idemp','firstname','midname',
                                                    'lastname','email','dob','idno','gender')}),

        ]

    inlines = [
        famemInline, certInline, whInline, pnInline
    ]

# Update User model
    def save_model(self, request, obj, form, change):
        email = obj.email
        username = obj.idemp
        first_name = obj.firstname
        last_name = obj.lastname
        if User.objects.filter(username=username).exists():
                #user = User.objects.create_user(username, '@vnsp.vn', password, is_staff=True)
            user = User.objects.get(username=username)
            user.email = email
            user.first_name = last_name
            user.last_name = first_name
            user.save()
                #group = Group.objects.get(name='employee')
                #user.groups.add(group)
                #messages.add_message(request, messages.INFO, 'Users were created!')
        super(epAdmin, self).save_model(request, obj, form, change)        

#   Remove fillter for normal user
    def get_list_filter(self, request):
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['sec','gender']
        else:
            return []
#   Lấy filter log health check
    def healthlog(self, obj):
        url = 'http://ess.vnsp.vn/eprofile/helthcheck/?q=' + obj.idemp
        #url = get_current_site(request) + '/eprofile/helthcheck/?q=' + obj.idemp
        #url = settings.SITE_URL + '/eprofile/helthcheck/?q=' + obj.idemp
        return format_html("<a href='%s'>%s</a>" % (url, url))
    healthlog.short_description = 'Lịch sử sức khỏe, click -->'
    healthlog.allow_tags = True

    def get_readonly_fields(self, request, obj=None):
        # if request.user.is_superuser:
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['image_tag','healthlog'] # Image field must be readonly for display in detail page, hyperlink (format_html) have to be readonly
        return self.readonly_fields

    def image_tag(self, obj):
        if obj.headshot and hasattr(obj.headshot, 'url'):
            #return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.headshot.url))
            return format_html('<img src="{0}" style="width: auto; height:200px;" />'.format(obj.headshot.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def thumbnail(self, obj):
        if obj.headshot and hasattr(obj.headshot, 'url'):
            return format_html('<img src="{0}" style="width: auto; height:100px;" />'.format(obj.headshot.url))

    thumbnail.short_description = 'avatar'
    thumbnail.allow_tags = True




# Remove normal user see the other persion
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)

# Remove action from normal user
    def get_actions(self, request):
        actions = super().get_actions(request)
        #if request.user.username[0].upper() != 'J':
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            if 'import_system_user' in actions:
                del actions['import_system_user']
                #del actions['import_system_user234']
        return actions




    def import_system_user(self,request,queryset):
        username='john'
        password='secret'
        email='abcd@vnsp.vn'
        for qe in queryset:
            username = qe.idemp
            password = qe.idno
            email = qe.email
            first_name = qe.lastname
            last_name = qe.firstname
            #user = User.objects.get(username=username)
            if not User.objects.filter(username=username).exists():
                #user = User.objects.create_user(username, '@vnsp.vn', password, is_staff=True)
                user = User.objects.create_user(username, email, password,first_name=first_name,last_name=last_name, is_staff=True)
                #user = User.objects.get(username=username,first_name=first_name,last_name=last_name,is_staff=True)
                #user.set_password(password)
                #user.save()
                group = Group.objects.get(name='employee')
                user.groups.add(group)
                messages.add_message(request, messages.INFO, 'Users were created!')
    import_system_user.short_description = "Thêm quyền truy cập, user = ID, pass = Số CMT"

admin.site.register(efile,epAdmin)

# Health check result

class hchkResource(resources.ModelResource):

    class Meta:
        model = helthcheck
class hchkAdmin(ImportExportModelAdmin):

    list_display = ('idemp','sec','fullname','dock','hlevel','conclus','advise')
    search_fields = ['idemp__idemp','dock','hlevel']
    sortable_by = ['dock','hlevel']
    #list_filter = ['sec','hlevel']
    list_display_links = ['idemp','sec','fullname','dock','hlevel','conclus','advise']
    resource_class = hchkResource
    # Remove normal user see the other person
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)
    

    #   Remove fillter for normal user
    def get_list_filter(self, request):
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['sec','hlevel']
        else:
            return []

admin.site.register(helthcheck,hchkAdmin)


class fmemResource(resources.ModelResource):

    class Meta:
        model = famem
        import_id_fields = ['idemp']
class fmemAdmin(ImportExportModelAdmin):
    list_display = ('idemp','mkind','fullname','gender','dob','remarks')
    sortable_by = ['gender','mkind']

    # Remove normal user from editing ID
    def get_readonly_fields(self, request, obj=None):
        # if request.user.is_superuser:
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['idemp'] # Image field must be readonly for display in detail page, hyperlink (format_html) have to be readonly
        return self.readonly_fields

    # Remove normal user from seeing the other person
    def get_queryset(self, request):

        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return super().get_queryset(request).filter(idemp=request.user.username)
        else:
            return super().get_queryset(request)
admin.site.register(famem,fmemAdmin)



