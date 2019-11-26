from django.contrib import admin
from .models import Child, Parent


@admin.register(Child)
class ChildrenAdmin(admin.ModelAdmin):
    fields = ('first_name', 'middle_name', 'last_name', 'dob', 'parent')
    date_hierarchy = 'created_at'
    search_fields = ['first_name', 'middle_name', 'last_name']
    list_display = ('full_name', 'parent_full_name', 'age', 'ph_class')
    list_filter = ('ph_class',)

    def full_name(self, obj):
        return obj.full_name()

    def parent_full_name(self, obj):
        return obj.full_name()


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    pass
