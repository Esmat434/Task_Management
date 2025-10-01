from django.test import TestCase
from django.contrib.auth import get_user_model

from tasks.models import (
    Category,Board,Task
)
from tasks.serializers import (
    CategoryCreateSerializer,CategoryUpdateSerializer,BoardCreateSerializer,BoardUpdateSerializer,
    TaskCreateSerializer,TaskUpdateSerializer
)

User=get_user_model()

class TestCategorySerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user,title='test this')
    
    def test_category_create_serializer(self):
        data = {
            'title':'test category'
        }
        serializer = CategoryCreateSerializer(data=data, user=self.user)
        self.assertEqual(serializer.is_valid(),True)
    
    def test_category_update_serializer(self):
        data = {
            'title':'change this'
        }
        serializer = CategoryUpdateSerializer(instance=self.category, data=data, user=self.user, partial=True)
        self.assertEqual(serializer.is_valid(),True)

class TestBoardSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user,title='test this')
        self.board = Board.objects.create(user=self.user, title='test this board', category=self.category)

    def test_board_create_serializer(self):
        data = {
            'title':'test board title',
            'category':self.category.pk
        }
        serializer = BoardCreateSerializer(data=data, user=self.user)
        self.assertEqual(serializer.is_valid(),True)

    def test_board_update_serializer(self):
        data = {
            'title':'change this'
        }
        serializer = BoardUpdateSerializer(instance=self.board, data=data, user=self.user, partial=True)
        self.assertEqual(serializer.is_valid(),True)

class TestTaskSerializer(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user,title='test this')
        self.board = Board.objects.create(user=self.user, title='test this board', category=self.category)
        self.task = Task.objects.create(user=self.user, board=self.board, title='task')

    def test_task_create_serializer(self):
        data = {
            'board':self.board.pk,
            'title':'test task',
            'description':'test description',
            'status':Task.TaskStatus.enable
        }
        serializer = TaskCreateSerializer(data=data, user=self.user)
        self.assertEqual(serializer.is_valid(),True)
    
    def test_task_update_serializer(self):
        data = {
            'title':'change this',
            'enable':Task.TaskStatus.disable
        }
        serializer = TaskUpdateSerializer(instance=self.task, data=data, user=self.user, partial=True)
        self.assertEqual(serializer.is_valid(),True)
