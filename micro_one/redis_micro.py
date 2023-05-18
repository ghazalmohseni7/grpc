import redis

redis_client=redis.Redis(host='127.0.0.1',port=6379,db=0)
client=redis_client.get('username')
print(client)

class CacheRedis():
    def __init__(self):
        self.redis_client=redis.Redis(host='127.0.0.1',port=6379,db=0)

    def set(self,cache_key,data):
        self.redis_client.set(cache_key,data,ex=20)
        return True

    def get(self,cache_key):
        cached_data=self.redis_client.get(cache_key)
        return cached_data
