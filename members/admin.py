from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'college', 'major', 'created_at']
    search_fields = ['name', 'email', 'college', 'major']
    list_filter = ['college', 'created_at']
    readonly_fields = ['created_at']