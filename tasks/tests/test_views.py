import json
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from tasks.models import (
    Category,Board,Task
)

User = get_user_model()

class TestCategoryCreateListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.client.force_login(user=self.user)
        self.data = {
            'title':'test category'
        }
    
    def test_category_list_valid_data(self):
        url = reverse('tasks:categories')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_category_create_valid_data(self):
        url = reverse('tasks:categories')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)

class TestCategoryDetailUpdateDestroyView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.client.force_login(user=self.user)
        self.update_data = {
            'title':'change category'
        }
    
    def test_category_detail_valid_data(self):
        url = reverse('tasks:category-detail', args=[self.category.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_category_put_valid_data(self):
        url =  reverse('tasks:category-detail', args=[self.category.pk])
        response = self.client.put(
            url, 
            data=json.dumps(self.update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
    
    def test_category_delete_valid_data(self):
        url = reverse('tasks:category-detail', args=[self.category.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

class TestBoardCreateListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.client.force_login(user=self.user)
        self.data = {
            'category':self.category.pk,
            'title':'test board'
        }
    
    def test_board_list_valid_data(self):
        url = reverse('tasks:boards')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_board_create_valid_data(self):
        url = reverse('tasks:boards')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)

class TestBoardDetailUpdateDestroyView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.board = Board.objects.create(user=self.user, title='test board', category=self.category)
        self.client.force_login(user=self.user)
        self.update_data = {
            'title':'change board'
        }
    
    def test_board_detail_valid_data(self):
        url = reverse('tasks:board-detail', args=[self.board.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_board_update_valid_data(self):
        url = reverse('tasks:board-detail', args=[self.board.pk])
        response = self.client.put(
            url, 
            data=json.dumps(self.update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
    
    def test_board_delete_valid_data(self):
        url = reverse('tasks:board-detail', args=[self.board.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

class TestTaskCreateListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.board = Board.objects.create(user=self.user, title='test board', category=self.category)
        self.client.force_login(user=self.user)
        self.data = {
            'board':self.board.pk,
            'title':'change board',
            'description':'this is good',
            'status':Task.TaskStatus.enable
        }
    
    def test_task_list_valid_data(self):
        url = reverse('tasks:tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_task_create_valid_data(self):
        url = reverse('tasks:tasks')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 201)

class TestTaskDetailUpdateDestroyView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.board = Board.objects.create(user=self.user, title='test board', category=self.category)
        self.task = Task.objects.create(user=self.user, board=self.board, title='test task')
        self.client.force_login(user=self.user)
        self.update_data = {
            'title':'change task',
            'enable':Task.TaskStatus.disable
        }
    
    def test_task_detail_valid_data(self):
        url = reverse('tasks:task-detail', args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_task_update_valid_data(self):
        url = reverse('tasks:task-detail', args=[self.task.pk])
        response = self.client.put(
            url, 
            data=json.dumps(self.update_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
    
    def tes_task_delete_valid_data(self):
        url = reverse('task:task-detail', args=[self.task.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

class TestTaskDisbaleListView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.client.force_login(user=self.user)
    
    def test_task_disable_list_valid_data(self):
        url = reverse('tasks:task-disable-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
class TestTaskDisableDetailView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='123456789'
        )
        self.category = Category.objects.create(user=self.user, title='book')
        self.board = Board.objects.create(user=self.user, title='test board', category=self.category)
        self.task = Task.objects.create(user=self.user, board=self.board, title='test task', status=Task.TaskStatus.disable)
        self.client.force_login(user=self.user)
    
    def test_task_disable_detail_valid_data(self):
        url = reverse('tasks:task-disable-detail', args=[self.task.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)