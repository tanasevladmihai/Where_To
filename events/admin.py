# events/admin.py
from django.contrib import admin
from .models import City, Category, Event

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'category', 'theme', 'start_date', 'end_date', 'is_active')
    list_filter = ('city', 'category', 'theme', 'start_date')  
    search_fields = ('name', 'address', 'description')  
    


