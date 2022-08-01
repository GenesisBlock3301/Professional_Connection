from django.contrib import admin
from .models import Company, Management, Experience


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "manager", "city", "industry"
    )


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "company", "position"
    )


@admin.register(Experience)
class ManagementAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "title", "employment_type", "start",
        "end", "position", "company"
    )
