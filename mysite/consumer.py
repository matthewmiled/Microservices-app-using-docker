import pika

params = pika.URLParameters('amqps://fjqexisa:juWr6KCA37QQZ4QlgFSANBgs81-5RTSv@rattlesnake.rmq.cloudamqp.com/fjqexisa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='mysite')

def callback(ch, method, properties, body):
    print('Received in mysite')
    print(body)


channel.basic_consume(queue='mysite', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

