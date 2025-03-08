import redis

# Connect to Redis
redis_host = "10.128.0.35"  # Replace with your Redis IP
redis_port = 6379

client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

channel = "test-channel"

while True:
    message = input("Enter message to publish: ")
    client.publish(channel, message)
