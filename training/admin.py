from django.contrib import admin
from .models import wclendar
from .models import tnsection
# Register your models here.
from django.utils.html import format_html
from .models import tnindex
from .models import isoindex, isodetail
from .models import iso9index, iso9detail

class tkcInline(admin.TabularInline):
    model = tnsection
    # exclude = ('short_description',)
    extra = 0

class tnidxAdmin(admin.ModelAdmin):
    #pass
    #exclude = ('section',)
    ordering = ['section']
    readonly_fields = ['section']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
            return []
        return self.readonly_fields

    # list_editable = ('section',)
    # list_display = ('doctitle','docfile')
    # ordering = ['doctitle']
    inlines = [
        tkcInline,
    ]
admin.site.register(tnindex,tnidxAdmin)


# ISO 14001
class isoInline(admin.TabularInline):
    model = isodetail
    # exclude = ('short_description',)
    extra = 0

class isoindexAdmin(admin.ModelAdmin):
    #pass
    #exclude = ('section',)
    ordering = ['stdname']
    readonly_fields = ['stdname']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
            return []
        return self.readonly_fields

    # list_editable = ('section',)
    # list_display = ('doctitle','docfile')
    # ordering = ['doctitle']
    inlines = [
        isoInline,
    ]
admin.site.register(isoindex,isoindexAdmin)

# ISO 9001

class iso9Inline(admin.TabularInline):
    model = iso9detail
    # exclude = ('short_description',)
    extra = 0

class iso9indexAdmin(admin.ModelAdmin):
    #pass
    #exclude = ('section',)
    ordering = ['stdname']
    readonly_fields = ['stdname']
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            #return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
            return []
        return self.readonly_fields

    # list_editable = ('section',)
    # list_display = ('doctitle','docfile')
    # ordering = ['doctitle']
    inlines = [
        iso9Inline,
    ]
admin.site.register(iso9index,iso9indexAdmin)





class wcAdmin(admin.ModelAdmin):
    list_display = ('doctitle','thumbnail')
    list_display_links = ['doctitle','thumbnail']
    readonly_fields = ['doctitle','image_tag']

    def get_readonly_fields(self, request, obj=None):
        if (request.user.is_superuser or request.user.groups.filter(name='hrad').exists()):
            return ['image_tag'] # Superuser is unlimited, imange_tag needed readonly property
        return self.readonly_fields

    def image_tag(self, obj):
        if obj.wcpic and hasattr(obj.wcpic, 'url'):
            return format_html('<img src="{0}" style="width: auto; height:260px;" />'.format(obj.wcpic.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def thumbnail(self, obj):
        if obj.wcpic and hasattr(obj.wcpic, 'url'):
            return format_html('<img src="{0}" style="width: auto; height:100px;" />'.format(obj.wcpic.url))

    thumbnail.short_description = 'thumbnail'
    thumbnail.allow_tags = True


admin.site.register(wclendar,wcAdmin)