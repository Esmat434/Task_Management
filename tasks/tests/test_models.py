from django.test import TestCase
from django.contrib.auth import get_user_model

from tasks.models import (
    Category,Board,Task
)

User = get_user_model()

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test',email='test@gmail.com',password='123456789')
        self.category = Category.objects.create(user=self.user, title='test category')
        self.board = Board.objects.create(user=self.user, title='test board', category=self.category,)
        self.task = Task.objects.create(
            user=self.user, 
            board=self.board, 
            title='test task', 
            description='test description',
            status=Task.TaskStatus.enable
        )

    def test_category_valid_data(self):
        self.assertEqual(self.category.user.username, 'test')
        self.assertEqual(self.category.title, 'test category')

    def test_board_valid_data(self):
        self.assertEqual(self.board.user.username, self.user.username)
        self.assertEqual(self.board.category.title, self.category.title)
        self.assertEqual(self.board.title, 'test board')
    
    def test_task_valid_date(self):
        self.assertEqual(self.task.user.username, self.user.username)
        self.assertEqual(self.task.board.title, self.board.title)
        self.assertEqual(self.task.title, 'test task')
        self.assertEqual(self.task.description, 'test description')
        self.assertEqual(self.task.status, Task.TaskStatus.enable)