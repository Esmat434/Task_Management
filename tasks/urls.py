from django.urls import path

from .views import (
    CategoryCreateListView,CategoryDetailUpdateDestroyView,BoardCreateListView,BoardDetailUpdateDestroyView,
    TaskCreateListView,TaskDisableListView,TaskDisableDetailView,TaskDetailUpdateDestroyView
)

app_name = "tasks"

urlpatterns = [
    path('categories/', CategoryCreateListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailUpdateDestroyView.as_view(), name='category-detail'),
    path('boards/', BoardCreateListView.as_view(), name='boards'),
    path('boards/<int:pk>/', BoardDetailUpdateDestroyView.as_view(), name='board-detail'),
    path('tasks/', TaskCreateListView.as_view(), name='tasks'),
    path('tasks/disable/', TaskDisableListView.as_view(), name="task-disable-list"),
    path("tasks/disable/<int:pk>/", TaskDisableDetailView.as_view(), name="task-disable-detail"),
    path('tasks/<int:pk>/', TaskDetailUpdateDestroyView.as_view(), name='task-detail')
]