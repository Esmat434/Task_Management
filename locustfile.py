from locust import HttpUser, task, between
import random
import time

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8081"
    wait_time = between(1, 5)  # شبیه‌سازی زمان بین درخواست‌ها

    def on_start(self):
        self.username = "testuser"
        self.password = "123456789"
        self.login()

    def login(self):
        response = self.client.post("/api/token/", json={
            "username": self.username,
            "password": self.password
        })
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access")
            self.refresh_token = data.get("refresh")
            self.token_expiry = time.time() + 60*5  
        else:
            print("Login failed")

    def refresh_access_token(self):
        response = self.client.post("/api/token/refresh/", json={
            "refresh": self.refresh_token
        })
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access")
            self.token_expiry = time.time() + 60*5
        else:
            print("Token refresh failed, re-login")
            self.login()

    def ensure_token(self):
        if time.time() >= getattr(self, "token_expiry", 0):
            self.refresh_access_token()

    def auth_headers(self):
        self.ensure_token()
        return {"Authorization": f"Bearer {self.access_token}"}

    @task(2)
    def view_profile(self):
        self.client.get(f"/api/profile/{self.username}/", headers=self.auth_headers())

    @task(3)
    def view_categories(self):
        self.client.get("/api/categories/", headers=self.auth_headers())

    @task(3)
    def view_boards(self):
        self.client.get("/api/boards/", headers=self.auth_headers())

    @task(4)
    def view_tasks(self):
        self.client.get("/api/tasks/", headers=self.auth_headers())

    @task(2)
    def view_tasks_disabled(self):
        self.client.get("/api/task_disable/", headers=self.auth_headers())

    @task(1)
    def register_random_user(self):
        rand = random.randint(1000, 999999)
        self.client.post("/api/register/", json={
            "username": f"user{rand}",
            "email": f"user{rand}@gmail.com",
            "password": "123456789",
            "confirm_password": "123456789"
        })

    @task(1)
    def login_random_user(self):
        rand = random.randint(1000, 999999)
        self.client.post("/api/token/", json={
            "username": f"user{rand}",
            "password": "123456789"
        })
