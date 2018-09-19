# Kafka Fraud Detector

This is your first real-world streaming application with Apache Kafka and Python — a real-time transaction fraud detection system.

This is the supporting repository for my blog post: [Building A Kafka Streaming Fraud Detection System In Python](https://blog.florimondmanca.com/building-a-kafka-streaming-fraud-detection-system-in-python).

## Install

This fraud detection system is fully containerised. You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it, but no other installation step is required.

## Quickstart

- Spin up your local single-node Kafka cluster:

```bash
$ docker-compose -f docker-compose.kafka.yml up
```

- Check the cluster is up and running:

```bash
$ docker-compose -f docker-compose.kafka.yml logs -f broker | grep "started"
```

- Start the transaction generator and the fraud detector:

```bash
$ docker-compose up
```

## Usage

Show a stream of transactions in the topic `T` (optionally add `--from-beginning`):

```bash
$ docker-compose -f docker-compose.kafka.yml exec kafka-console-consumer --bootstrap-server localhost:9092 --topic T
```

Topics:

- `queuing.transactions`: raw generated transactions
- `streaming.transactions.legit`: legit transactions
- `streaming.transactions.fraud`: suspicious transactions

Example transaction message:

```json
{"source": "yGfZ1Xa6k1r0", "target": "N5RvY7RO5sQF", "amount": 217.46, "currency": "EUR"}
```
