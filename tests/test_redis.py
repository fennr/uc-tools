import pytest
from uc_tools.redis import Redis


def connect_to_redis():
    host = "localhost"
    port = "6379"
    username = ""
    password = ""
    return Redis(host, port, username, password)


class TestRedisDB:
    redis_db = connect_to_redis()
    def test_connect(self):
        assert self.redis_db.client.ping()

    def test_get(self):
        key = "test_get"
        value = "test_value"
        self.redis_db.set(key, value)
        assert self.redis_db.get(key) == value

    def test_set(self):
        key = "test_set"
        value = "test_value"
        assert self.redis_db.set(key, value)

    def test_delete(self):
        key = "test_delete"
        value = "test_value"
        self.redis_db.set(key, value)
        assert self.redis_db.delete(key)
