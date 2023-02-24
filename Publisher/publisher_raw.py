import pika as pk


connection_parameters = pk.ConnectionParameters(
    host="localhost",
    # port="5762"
)

channel = pk.BlockingConnection(connection_parameters).channel()

channel.exchange_declare(exchange='data_exchange', exchange_type='direct')

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="wesley",
    # properties=pk.BasicProperties(
    # delivery_mode=2
    # )
)
