"""Produce fake transactions into a Kafka topic."""

import os
from time import sleep
import json

from kafka import KafkaProducer
from transactions import Transaction

TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while True:
        transaction: dict = Transaction.random().serialize()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)
        sleep(SLEEP_TIME)
