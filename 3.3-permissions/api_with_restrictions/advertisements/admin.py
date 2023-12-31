from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creator', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'creator__username')
    list_filter = ('status',)
    date_hierarchy = 'created_at'
