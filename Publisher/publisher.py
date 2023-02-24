from typing import Dict
import pika as pk
import json


class RabbitmqPublisher:

    def __init__(self) -> None:
        self.__host = "localhost"
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "data_exchange"
        self.__routing_key = ""
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
        return channel

    def sendMesseger(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pk.BasicProperties(
                delivery_mode=2
            )
        )


rabbitmq_publisher = RabbitmqPublisher()
rabbitmq_publisher.sendMesseger({"ola": "mundo"})
