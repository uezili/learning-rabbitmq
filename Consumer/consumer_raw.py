import pika as pk


def my_callback(ch, method, properties, body):
    print(body)


data_queueQue = "data_queue"
data_exchangeExc = "data_exchange"
connection_parameters = pk.ConnectionParameters(
    host='localhost'
)

channel = pk.BlockingConnection(connection_parameters).channel()
channel.exchange_declare(exchange="data_exchange", exchange_type="direct")
channel.queue_declare(
    queue="data_queue",
    durable=True
)

channel.basic_consume(
    queue=data_queueQue,
    auto_ack=True,
    on_message_callback=my_callback
)

print("Listen RebbitMQ")
channel.start_consuming()
