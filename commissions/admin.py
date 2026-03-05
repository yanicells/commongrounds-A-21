from django.contrib import admin
from .models import *


class CommissionTypeAdmin(admin.ModelAdmin):
    model = CommissionType


class CommissionTypeInline(admin.TabularInline):
    model = CommissionType


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommissionTypeInline,]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(CommissionType, CommissionTypeAdmin)