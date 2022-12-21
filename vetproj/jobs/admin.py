from django.contrib import admin
from .models import Job, Aplicant
# Register your models here.


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ['title', 'created', 'updated']

    def get_readonly_fields(self, request, obj: None):
        if obj:
            return ('title', 'created', 'updated')
        return ()


@admin.register(Aplicant)
class AplicantAdmin(admin.ModelAdmin):
    model = Aplicant
    list_display = ['first_name', 'last_name',
                    'email', 'website',
                    'employment_type', 'start_date',
                    'available_days', 'desired_hourly_wage',
                    'cover_letter', 'job', 'created', 'updated']

    def get_readonly_fields(self, request, obj: None):
        if obj:
            return ('first_name', 'last_name',
                    'email', 'website',
                    'employment_type', 'start_date',
                    'available_days', 'desired_hourly_wage',
                    'cover_letter', 'job', 'created', 'updated')
        return ()
