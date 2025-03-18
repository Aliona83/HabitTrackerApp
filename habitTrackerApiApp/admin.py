from django.contrib import admin
from .models import Tracker

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'frequency', 'specific_date', 'created_at')
    search_fields = ('title', 'user__username')  
    list_filter = ('frequency', 'created_at')  
    ordering = ('-created_at',) 
    fields = ('title', 'user', 'frequency', 'specific_date')  
    autocomplete_fields = ('user',)  

admin.site.register(Tracker, TrackerAdmin)
