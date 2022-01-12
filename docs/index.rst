.. IRIP API documentation master file, created by
   sphinx-quickstart on Wed Jan 12 23:35:55 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to IRIP
====================================

IRan Place Img API

.. toctree::
   :maxdepth: 2
   :caption: Contents:

IRPI is a **RESTful** API. your can download Iran beautiful Place img.

Example
------------

Find Random img ::

   $ curl IRPI.com.api/v1/random


::

   {
   "data": {
      "description": "description", 
      "location": "location", 
      "name": "example", 
      "photographer": "the photographer", 
      "sender": "sender"
   }, 
   "id": "uuid4", 
   "img name": "example", 
   "img url": "http://localhost:5000/img/example/image.jpg", 
   "status": "ok"
   }

Find img by name ::

   $ curl IRPI.com/v1/find/example

::

   {
   "data": {
      "description": "description", 
      "location": "location", 
      "name": "example", 
      "photographer": "the photographer", 
      "sender": "sender"
   }, 
   "id": "uuid4", 
   "img name": "example", 
   "img url": "http://localhost:5000/img/example/image.jpg", 
   "status": "ok"
   }


