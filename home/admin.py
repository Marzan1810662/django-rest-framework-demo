from django.contrib import admin
from .models import Person

@admin.action(description='Make all names upper case')
def make_uppercase(modeladmin,request,queryset):
    print('********')
    print(queryset)
    queryset.update(name=queryset.values_list('name',flat=True)[0].upper())


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']
    ordering = ['name']
    actions= [make_uppercase] #reference of thr make_uppercase function


# admin.site.register(Person)
admin.site.register(Person, PersonAdmin)