# Redis Pub/Sub Example

This project demonstrates a simple implementation of Redis Pub/Sub (Publisher-Subscriber) using Python.

## Prerequisites

- Python 3.x
- Redis server running (Ensure Redis is installed and running on your machine or server)
- `redis-py` library installed

To install the required library, run:
```sh
pip install redis
```

## Project Structure

```
├── publisher.py        # Publishes messages to the Redis channel
├── subscriber.py       # First subscriber listening to the channel
├── subscriber2.py      # Second subscriber listening to the channel
├── subscriber3.py      # Third subscriber listening to the channel
├── README.md           # Project documentation
```

## Configuration

Ensure the Redis server is running and update the `redis_host` variable in all scripts with the correct Redis IP.

```python
redis_host = "10.128.0.35"  # Replace with your Redis server IP
redis_port = 6379
```

Additionally, modify the Redis configuration file (`redis.conf`) to allow external connections by setting:
```sh
bind 0.0.0.0
```
Also, configure the firewall settings to allow Redis connections.

## How to Use

### 1. Start Subscribers

Open multiple terminal windows and run the subscribers:
```sh
python3 subscriber.py
python3 subscriber2.py
python3 subscriber3.py
```

Each subscriber will wait for messages published to the channel `test-channel`.

### 2. Start the Publisher

Run the publisher script in another terminal:
```sh
python3 publisher.py
```

Enter messages in the terminal, and they will be broadcasted to all subscribers.

## Expected Output

Subscribers will display:
```
Subscriber 1 received: Hello, Redis!
Subscriber 2 received: Hello, Redis!
Subscriber 3 received: Hello, Redis!
```

## Notes

- Ensure Redis is running before executing the scripts.
- Subscribers will receive messages in real-time when published.
- You can modify the `channel` name if needed.

## License

This project is open-source and available under the MIT License.

