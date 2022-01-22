import pika
import json

params = pika.URLParameters('amqps://fjqexisa:juWr6KCA37QQZ4QlgFSANBgs81-5RTSv@rattlesnake.rmq.cloudamqp.com/fjqexisa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):

    properties = pika.BasicProperties(method)

    channel.basic_publish(exchange='', routing_key='mysite', body=json.dumps(body), properties=properties)
