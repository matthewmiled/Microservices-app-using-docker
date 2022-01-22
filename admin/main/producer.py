import pika

params = pika.URLParameters('amqps://fjqexisa:juWr6KCA37QQZ4QlgFSANBgs81-5RTSv@rattlesnake.rmq.cloudamqp.com/fjqexisa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='mysite', body='hello message from admin app to mysite app')
