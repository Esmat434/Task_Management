from django.contrib import admin

from .models import (
    Category,Board,Task
)
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','created_at']

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','category','created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','board','title','status','published_at','created_at']