from django.contrib import admin
from .models import *


class CommissionAdmin(admin.ModelAdmin):
    model = Commission


class CommissionInline(admin.TabularInline):
    model = Commission


class CommissionTypeAdmin(admin.ModelAdmin):
    model = CommissionType
    inlines = [CommissionInline,]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(CommissionType, CommissionTypeAdmin)