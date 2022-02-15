from django.contrib import admin
from .models import *

#@admin.register(PVM,OChart,WPost,SET)
# class PVMAdmin(admin.ModelAdmin):
#     pass


# class FAQAdmin(admin.ModelAdmin): 



#     pass
#     ordering = ('-topic',)
class FAQInline(admin.TabularInline):
    model = FAQDetail
    # exclude = ('short_description',)
    extra = 0
class FAQAdmin(admin.ModelAdmin):
    pass
    ordering = ['topic',]

    inlines = [
        FAQInline,
    ]

    # class Media:
    #     css = {
    #         'all': ('admin/css/custom_admin.css', )     # Include extra css
    #     }
admin.site.register(FAQ,FAQAdmin)

class PVMAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(PVM,PVMAdmin)

class OChartAdmin(admin.ModelAdmin):
    pass
admin.site.register(OChart,OChartAdmin)

class WPostAdmin(admin.ModelAdmin):
    pass
    ordering = ['title',]
admin.site.register(WPost,WPostAdmin)

class SETAdmin(admin.ModelAdmin):
    list_display = ('fname','email',)
    list_editable = ['email',]
admin.site.register(SET,SETAdmin)

class QnAAdmin(admin.ModelAdmin):

    list_display = ('idemp','idate','quest','answ',)
    ordering = ['idate',]
    
    # Record questioner
    def save_model(self, request, obj, form, change):
        obj.idemp = request.user
        super().save_model(request, obj, form, change)
    # employee can not edit answer

    def get_readonly_fields(self, request, obj=None):
        if not (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['idemp','answ','idate'] 
        return self.readonly_fields

admin.site.register(QnA,QnAAdmin)