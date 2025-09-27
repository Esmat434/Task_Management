from django.test import SimpleTestCase
from django.urls import reverse

class TestUrls(SimpleTestCase):
    def test_category_list_url(self):
        url = reverse('tasks:categories')
        self.assertEqual(url, '/api/categories/')
    
    def test_category_detail_url(self):
        url = reverse('tasks:category-detail', args=[1])
        self.assertEqual(url, f'/api/categories/{1}/')
    
    def test_board_list_url(self):
        url = reverse('tasks:boards')
        self.assertEqual(url, '/api/boards/')
    
    def test_board_detail_url(self):
        url = reverse('tasks:board-detail', args=[1])
        self.assertEqual(url, f'/api/boards/{1}/')
    
    def test_task_list_url(self):
        url = reverse('tasks:tasks')
        self.assertEqual(url, '/api/tasks/')
    
    def test_task_detail_url(self):
        url = reverse('tasks:task-detail', args=[1])
        self.assertEqual(url, f'/api/tasks/{1}/')
    
    def test_task_disable_list_url(self):
        url = reverse('tasks:task-disable-list')
        self.assertEqual(url, '/api/tasks/disable/')
    
    def test_tasks_disable_detail_url(self):
        url = reverse('tasks:task-disable-detail', args=[1])
        self.assertEqual(url, f'/api/tasks/disable/{1}/')