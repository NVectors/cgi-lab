#!/usr/bin/env python3

import os
import json

print("Content-Type: text/plain")
print("")

# Q1 Inspect all environment variables
# os.environ returns a dictionary=> environment variables: value
print(os.environ)

# Q2 Serve the environment back as JSON
print("Content-Type: application/json")
print("")
# Convert os.environ object into json string
json_object = json.dumps(dict(os.environ), indent=1)
print(json_object)

# Q2 Return values of the query parameter
param = "QUERY_STRING"
print("%s: %s" % (param, os.environ[param]))

# Q3 Return value of the user's browser
param = "HTTP_USER_AGENT"
print("%s: %s" % (param, os.environ[param]))

####################################################################################################
from templates import login_page, secret_page, after_login_incorrect
import secret
import cgi, cgitb
from http.cookies import SimpleCookie

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

cgitb.enable()

# Q4 POSTed data to the CGI script
#print(login_page())
form = cgi.FieldStorage()

# Get the data from the form fields
usernameEntered = form.getvalue('username')
passwordEntered = form.getvalue('password')

form_ok = (usernameEntered == secret.username and passwordEntered == secret.password)

#Q5 Set a cookie if login is correct
param = "HTTP_COOKIE"
cookie = SimpleCookie(os.environ[param])
# By default
cookie_username = None
cookie_password = None
# Set cookie
if cookie.get("username"):
   cookie_username = cookie.get("username").value
if cookie.get("password"):
   cookie_password = cookie.get("password").value

cookie_ok = (cookie_username == secret.username and cookie_password == secret.password)

# Check for cookie
if (cookie_ok):
    usernameEntered = cookie_username
    passwordEntered = cookie_password

print("Content-Type: text/html")

# Check login info
if (form_ok):
    # Set the cookie
    print("Set-Cookie: username=", usernameEntered)
    print("Set-Cookie: password=", passwordEntered)
print("")

if (not usernameEntered and not passwordEntered):
    print(login_page())
elif (form_ok):
    print(secret_page(usernameEntered, passwordEntered))
else:
    print(after_login_incorrect())

