# Learning about Apache Kafka
## Docker Image for Kafka
https://hub.docker.com/r/bitnami/kafka

## Basic commands

### Create Topic
```./kafka-topics.sh --create --topic <topic_name> --bootstrap-server localhost:9092```

### List Topics
```./kafka-topics.sh --list --bootstrap-server localhost:9092```

### Describe a topic
```./kafka-topics.sh --describe --topic <topic_name> --bootstrap-server localhost:9092```\
```./kafka-console-consumer.sh --topic <topic_name>  --bootstrap-server localhost:9092```

### Check Consumer Offset
```./kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group <group_id>```
