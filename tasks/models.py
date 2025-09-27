from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories', verbose_name='User')
    title = models.CharField(max_length=150, verbose_name='Title')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards', verbose_name='User')
    title = models.CharField(max_length=155, verbose_name='Title')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='boards', null=True, blank=True, verbose_name='Category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'

class Task(models.Model):
    class TaskStatus(models.TextChoices):
        enable = 'Enable'
        disable = 'Disable'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='User')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks', verbose_name='Board')
    title = models.CharField(max_length=155, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    status = models.CharField(max_length=10, choices=TaskStatus, default=TaskStatus.enable, verbose_name='Status')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Published Date')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Created Date')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'