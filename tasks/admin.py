from django.contrib import admin
from tasks.models import Category, Tasks
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "category"]
    list_display_links = ["title", "description", "category"]