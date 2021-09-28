from kafka import KafkaConsumer


# define a consumer taht waits for new messages
def kafka_python_consumer():
    
    # using the topic name and setting a group id
    consumer = KafkaConsumer('testtopic', group_id='pythonconsumer', bootstrap_servers='localhost:9092',)
    for message in consumer:
        print(message)

print("start consuming")

# start
kafka_python_consumer()

print("done")