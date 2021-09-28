from kafka import KafkaProducer

message = 'Test messsage: Hello World!'

# Create producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

#send message into Kafka
def kafka_python_producer_async(producer, message):
    producer.send('testtopic', message).add_callback(success).add_errback(error)
    producer.flush()
    
    
def success(metadata):
    print(metadata.topic)

def error(exception):
    print(exception)

print("start producing")


kafka_python_producer_async(producer, bytes(message, 'utf-8'))

print("done")