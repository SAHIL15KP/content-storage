from django.contrib import admin
from .models import UserFile

@admin.register(UserFile)
class UserFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'content_type', 'uploaded_at']
    list_filter = ['content_type', 'uploaded_at']
    search_fields = ['name', 'user__username', 'user__email']
