# Microservices-app-using-docker
A test project to showcase how 2 separate apps made with Django can be containerised in Docker and communicate via RabbitMQ.

Making an API call using the end points below will update the 'admin' database, which will in turn update the database for the 'mysite' app using messaging with RabbitMQ. 

---

## Docker Usage

* `admin` app is made in Django and ran within a docker container on port 8000 - see docker-compose.yml within the `admin` folder
* `mysite` app is made in Django and ran within a docker container on port 8001 - see docker-compose.yml within the `mysite` folder

* Build images by running `docker-compose up --build` in the command line within each of the app directories

---

## API Usage

### GET request to list all blog posts

**Request**

* `GET /api/blogposts`

**Response**

* `200 OK` on success

```
[
  {
    "id": 1,
    "title": "blogpost1",
    "image": "image1",
    "likes": 0
  },
  {
    "id": 2,
    "title": "blogpost2",
    "image": "image2",
    "likes": 0
  }
]
```
---

### POST request to create a new blog post

**Request**

* `POST /api/blogposts`

**Arguments**

* `"title":string` - a title for the blog post
* `"image":string` - an image url for the blog post

**Response**

* `400 BAD REQUEST` if invalid data posted
* `201 CREATED` on success

---

### GET request to retrieve specific blog post

**Request**

* `GET /api/blogposts/<str:id>`

**Response**

* `404 NOT FOUND` if the blog post does not exist
* `200 OK` on success

```
{
  "id": 1,
  "title": "blogpost1",
  "image": "image1",
  "likes": 0
}
```
---

### PUT request to update specific blog post

**Request**

* `PUT /api/blogposts/<str:id>`

**Arguments**

* `"title":string` - a title for the blog post
* `"image":string` - an image url for the blog post

**Response**

* `400 BAD REQUEST` if invalid data posted
* `404 NOT FOUND` if the blog post does not exist
* `202 ACCEPTED` on success

```
{
  "id": 1,
  "title": "updated_blogpost1",
  "image": "updayed_image1",
  "likes": 0
}
```
---

### DELETE request to delete specific blog post

**Request**

* `DELETE /api/blogposts/<str:id>`

**Response**

* `404 NOT FOUND` if the blog post does not exist
* `204 NO CONTENT` on success

---


