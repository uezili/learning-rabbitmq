import pika as pk


class RabbitmqConsumer:
    def __init__(self, callback) -> None:
        self.__host = "localhost"
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
        connection_parameters = pk.ConnectionParameters(
            host=self.__host,
            credentials=pk.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pk.BlockingConnection(connection_parameters).channel()
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            on_message_callback=self.__callback
        )
        return channel

    def start(self):
        print("Listen RebbitMQ")
        self.__channel.start_consuming()


def my_callback(ch, method, properties, body):
    print(body)


rabbitmq_Consumer = RabbitmqConsumer(my_callback)
rabbitmq_Consumer.start()
