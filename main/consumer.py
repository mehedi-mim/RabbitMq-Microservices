import json

import pika

from main import Product, db

params = pika.URLParameters('amqps://fnsuivrm:ljL6QoPSve-RjORP33IlZn4fwpluopAw@woodpecker.rmq.cloudamqp.com/fnsuivrm')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(body)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product created')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()
channel.close()
