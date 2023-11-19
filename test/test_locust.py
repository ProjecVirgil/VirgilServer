"""File locust conf."""
from locust import HttpUser, task, between

class MyUser(HttpUser):
    """A single user that sends requests to the server.

    Args:
        HttpUser (_type_): _description_
    """
    wait_time = between(1, 2)

    @task
    def synchronous(self):
        """Test task synchronous."""
        self.client.get("/synchronous")

    @task
    def asynchronous(self):
        """Test task asynchronous."""
        self.client.get("/asynchronous")


#command test locust -f test_locust.py --web-host=127.0.0.1 --web-port=1111