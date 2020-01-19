from django.contrib import admin

from .models import Child, Parent, Facilitator


# Register your models here
# TODO:make custom form for users
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#   pass


@admin.register(Child)
class ChildrenAdmin(admin.ModelAdmin):
    fields = ('first_name', 'middle_name', 'last_name', 'stage', 'special_needs', 'dob', 'parent')
    date_hierarchy = 'created_at'
    search_fields = ['first_name', 'middle_name', 'last_name']
    list_display = ('full_name', 'parent_full_name', 'age', 'ph_class')
    list_filter = ('ph_class', 'special_needs')

    def full_name(self, obj):
        return obj.full_name()

    def parent_full_name(self, obj):
        return obj.full_name()


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'middle_name', 'last_name',
              'email', 'pri_phone_no', 'sec_phone_no', 'neighbourhood')
    date_hierarchy = 'created_at'
    search_fields = ['first_name', 'last_name', 'neighbourhood']
    list_display = ('full_name', 'email', 'pri_phone_no', 'sec_phone_no', 'neighbourhood')
    list_filter = ('neighbourhood',)

    def full_name(self, obj):
        return obj.full_name()


@admin.register(Facilitator)
class FacilitatorAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'middle_name', 'last_name', 'email', 'ph_class')
    date_hierarchy = 'created_at'
    search_fields = ['first_name', 'last_name', ]
    list_display = ('full_name', 'email')

    def full_name(self, obj):
        return obj.full_name()
