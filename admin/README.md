# Microservices-app-using-docker
An blog web app made with Django and mysql that is run in Docker containers.

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


