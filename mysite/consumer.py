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
        
        try:
            blogpost = BlogPost(id=data['id'], title=data['title'], image=data['image'])
            print("Blogpost created")
            blogpost.save()
        
        except BlogPost.DoesNotExist:
            print("Not found")

    elif properties.content_type == 'blogpost_updated':

        ## THIS GET REQUEST PART ISN'T QUITE WORKING (CANNOT FIND BLOGPOST WITH ID THAT IS PASSED)

        try:
            blogpost = BlogPost.objects.get(id=data['id'])
            blogpost.title = data['title']
            blogpost.image = data['image']
            print("Blogpost updated")
            blogpost.save()

        except BlogPost.DoesNotExist:
            print("Not found")

    elif properties.content_type == 'blogpost_deleted':

        try:
            blogpost = BlogPost.objects.get(id=data)
            print("Blogpost deleted")
            blogpost.delete()
        except BlogPost.DoesNotExist:
            print("Not found")


                
        
        
        

channel.basic_consume(queue='mysite', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

