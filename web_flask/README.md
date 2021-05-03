# 0x04. AirBnB clone - Web framework

## What is a Web Framework

Web frameworks are a piece of software that offers a way to create and run web applications. Thus, you don’t need to code on your own and look for probable miscalculations and faults.

## How to build a web framework with Flask

    Step 0: Installing Flask (this tutorial doesn’t cover Python and PIP installation)
    Step 1: Building the App structure
    Step 2: Creating the Main App code with the API request
    Step 3: Creating the 2 pages for the App (Main and Result) with Jinja, HTML, and CSS
    Step 4: Deploying and testing on your local laptop
    Step 5: Deploying on Google Cloud.

## How to define routes in Flask

Use decorator **route()** to link a function with an URL direction

## What is a route

outing or router in web development is a mechanism where HTTP requests are routed to the code that handles them. To put simply, in the Router you determine what should happen when a user visits a certain page.

Here is a simple routing example from Laravel. When someone opens the website’s /test/ subpage, it will display a Hello World text.

```
Route::get('/test', function () { 
    return 'Hello World';
});
```

## How to handle variables in a route

Your function then receives the as a keyword argument. Optionally, you can use a converter to specify the type of the argument like .<variable_name><variable_name><converter:variable_name>

example:
```
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```

## What is a template

emplate is a class of String module. It allows for data to change without having to edit the application. It can be modified with subclasses.

## How to create a HTML response in Flask by using a template
<h1 align=center>Rendering Templates </h1>
Generating HTML from within Python is not fun, and actually pretty cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically.

To render a template you can use the render_template() method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments. Here’s a simple example of how to render a template:

```
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```
```
/application.py
/templates
    /hello.html
```

## How to create a dynamic template (loops, conditions…)
For templates you can use the full power of Jinja2 templates. Head over to the official Jinja2 Template Documentation for more information.

Here is an example template:
```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```
## How to display in HTML data from a MySQL database