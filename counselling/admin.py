from django.contrib import admin

from .models import Career, GuidanceSession

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Show these fields in the admin panel
    search_fields = ('name',)  # Allow searching by career name

@admin.register(GuidanceSession)
class GuidanceSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'career', 'session_date')  # Show these fields
    list_filter = ('session_date', 'career')  # Add filters
    search_fields = ('user__username', 'career__name')  # Enable search

# Alternative way to register models (without decorators)
# admin.site.register(Career, CareerAdmin)
# admin.site.register(GuidanceSession, GuidanceSessionAdmin)

from django.contrib import admin
from .models import CareerCounselor, CareerSession

@admin.register(CareerCounselor)
class CareerCounselorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'contact_email')
    search_fields = ('full_name', 'specialization')

@admin.register(CareerSession)
class CareerSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'counselor', 'date', 'time', 'seats_available')
    list_filter = ('date', 'counselor')
    search_fields = ('title', 'counselor__full_name')

# Register your models here.
