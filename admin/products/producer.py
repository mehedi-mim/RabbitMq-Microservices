import pika, json

params = pika.URLParameters('amqps://fnsuivrm:ljL6QoPSve-RjORP33IlZn4fwpluopAw@woodpecker.rmq.cloudamqp.com/fnsuivrm')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
