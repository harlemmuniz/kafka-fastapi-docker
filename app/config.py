import asyncio

# env Variable
KAFKA_BOOTSTRAP_SERVERS = "localhost:9093"
KAFKA_TOPIC = "stargate-spark"
KAFKA_CONSUMER_GROUP = "group-id"
loop = asyncio.get_event_loop()
