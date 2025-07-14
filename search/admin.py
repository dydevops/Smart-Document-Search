from django.contrib import admin
from .models import Document

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'uploaded_at')
    search_fields = ('title', 'user__username')
    list_filter = ('uploaded_at',)
