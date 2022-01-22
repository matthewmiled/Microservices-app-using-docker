import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from main.models import BlogPost



params = pika.URLParameters('amqps://fjqexisa:juWr6KCA37QQZ4QlgFSANBgs81-5RTSv@rattlesnake.rmq.cloudamqp.com/fjqexisa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='mysite')

def callback(ch, method, properties, body):
    print('Received in mysite')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'blogpost_created':
        blogpost = BlogPost(id=data['id'], title=data['title'], image=data['image'])
        
        blogpost.save()

    elif properties.content_type == 'blogpost_updated':
        blogpost = BlogPost.objects.get(id=data['id'])
        blogpost.title = data['title']
        blogpost.image = data['image']

        blogpost.save()

    elif properties.content_type == 'blogpost_deleted':
        blogpost = BlogPost.objects.get(id=data)
        blogpost.delete()


                
        
        
        

channel.basic_consume(queue='mysite', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

