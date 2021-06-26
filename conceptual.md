### Conceptual Exercise (With comments from sunny in italics)

Answer the following questions below:

###What are important differences between Python and JavaScript?
JavaScript is a scripting language for web development. Python is more high level programming language in backend side.

###Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
The implementation of defaultdict is faster than get() or setdefault().

1. import collections
dictionary1 = collections.defaultdict('c' : 'Key Not found')

2. dictionary2 = {"a": 1, "b": 2} 
dictionary2.get("c", None) 

###What is a unit test? 
Unit testing is a type of testing to check if the small piece of code is doing what it is suppose to do. 

###What is an integration test? 
Integration testing is a type of testing to check if different pieces of the modules are working together. 

###What is the role of web application framework, like Flask?
web application frameworks like flask help easy to coding in backend without javascrips and ajax. It can help us shorten the code and easy to organize the webpage.

_Organization is one part, the other things it does is handle listening for HTTP requests, and creating responses to those requests. The job of the server is basically to serve up the files and content down to the client_
###You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like'foods?type=pretzel'). How might you choose which one is a better fitfor an application? 
I will use route URL, it is easy to read for users and developers.
_Routes make more sense for overall organization, but query parameters are used for things like smaller adjustments (changing the sort for example)_
###How do you collect data from a URL placeholder parameter using Flask? 
from flask import request
request.get('')

###How do you collect data from the query string using Flask? 
request.args

###How do you collect data from the body of the request using Flask? 
request.data, if you want to get forms, files can also used request.form, request.files

###What is a cookie and what kinds of things are they commonly used for? 
Cookie is smaller than session. It is txt file stores in the browsers. It usually to identify the log in status of the users.
_Not exactly. In fact, the default setting in Flask is to use cookies to store session. A cookie is stored, and shared between client's browser and directly manipulated by the server's headers._
###What is the session object in Flask? 
The session object in flask is used to track the session data. Session data in Flask session is a dictionary object that contains a key-value pair of the session variables and their associated values.

###What does Flask's `jsonify()` do? 
Since json is in string. jsonify()can help us convert into a string.
_jsonify SERIALIZES an **object in memory** into a string_
