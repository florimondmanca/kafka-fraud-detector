# Kafka Fraud Detector

This is your first real-world streaming application with Kafka and Python — a simple real-time fraud detection system.

This is the supporting repository for the blog post: [Building Your First Real-World Kafka Streaming Application in Python](https://blog.florimondmanca.com/building-your-first-real-world-kafka-streaming-application-in-python).

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

- Start the transaction producer and the fraud detection consumer:

```bash
$ docker-compose up
```

## Usage

- Show the stream of messages in the `transactions` topic (optionally add `--from-beginning`):

```bash
$ docker-compose -f docker-compose.kafka.yml exec kafka-console-consumer --bootstrap-server localhost:9092 --topic transactions
```

- Show the stream of suspicious transactions:

```
$ docker-compose logs -f detector
```
