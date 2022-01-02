import pika

params = pika.URLParameters('amqps://fnsuivrm:ljL6QoPSve-RjORP33IlZn4fwpluopAw@woodpecker.rmq.cloudamqp.com/fnsuivrm')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main!')
