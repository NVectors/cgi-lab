#!/usr/bin/env python3

import os
import json

print("Content-Type: text/plain")
print("")
print("<p> Hello World <p>")

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
for param in os.environ.keys():
    if param == "QUERY_STRING":
        print("%s: %s" % (param, os.environ[param]))

# Q3 Return value of the user's browser
for param in os.environ.keys():
    if param == "HTTP_USER_AGENT":
        print("%s: %s" % (param, os.environ[param]))