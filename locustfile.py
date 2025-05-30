from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def get_concerts(self):
        self.client.get("/concerts")

    @task
    def buy_ticket(self):
        self.client.post("/buy", json={"concert_id": 1, "quantity": 1})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 1000  # 1 second
    max_wait = 3000  # 3 seconds
