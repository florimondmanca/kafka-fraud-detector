# Kafka Fraud Detector

[![Kafka](https://img.shields.io/badge/streaming_platform-kafka-black.svg?style=flat-square)](https://kafka.apache.org)
[![Docker Images](https://img.shields.io/badge/docker_images-confluent-orange.svg?style=flat-square)](https://github.com/confluentinc/cp-docker-images)
[![Python](https://img.shields.io/badge/python-3.5+-blue.svg?style=flat-square)](https://www.python.org)

This is the supporting repository for my blog post: [Building A Streaming Fraud Detection System With Kafka And Python](https://blog.florimondmanca.com/building-a-streaming-fraud-detection-system-with-kafka-and-python).

## Install

This fraud detection system is fully containerised. You will need [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/) to run it.

You simply need to create a Docker network called `kafka-network` to enable communication between the Kafka cluster and the apps:

```bash
$ docker network create kafka-network
```

All set!

## Quickstart

- Spin up the local single-node Kafka cluster (will run in the background):

```bash
$ docker-compose -f docker-compose.kafka.yml up -d
```

- Check the cluster is up and running (wait for "started" to show up):

```bash
$ docker-compose -f docker-compose.kafka.yml logs -f broker | grep "started"
```

- Start the transaction generator and the fraud detector (will run in the background):

```bash
$ docker-compose up -d
```

## Usage

Show a stream of transactions in the topic `T` (optionally add `--from-beginning`):

```bash
$ docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic T
```

Topics:

- `queuing.transactions`: raw generated transactions
- `streaming.transactions.legit`: legit transactions
- `streaming.transactions.fraud`: suspicious transactions

Example transaction message:

```json
{"source": "yGfZ1Xa6k1r0", "target": "N5RvY7RO5sQF", "amount": 217.46, "currency": "EUR"}
```

## Teardown

To stop the transaction generator and fraud detector:

```bash
$ docker-compose down
```

To stop the Kafka cluster (use `down`  instead to also remove contents of the topics):

```bash
$ docker-compose -f docker-compose.kafka.yml stop
```

To remove the Docker network:

```bash
$ docker network rm kafka-network
```
