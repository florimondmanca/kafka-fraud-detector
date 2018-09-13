"""Example Kafka consumer."""

import os
import json

from kafka import KafkaConsumer

TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')


def is_suspicious(transaction: dict) -> bool:
    return transaction['amount'] >= 900


if __name__ == '__main__':
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    for message in consumer:
        transaction = message.value
        if is_suspicious(transaction):
            print({'type': 'potential_fraud', 'transaction': transaction})
